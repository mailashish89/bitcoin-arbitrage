import logging
import json
import redis
import urllib.parse
from arbitrage import config
from arbitrage.observers.traderbot import TraderBot


class MockMarket(object):
    def __init__(self, name, fee=0, usd_balance=500., btc_balance=15.,
                 persistent=True):
        self.name = name
        self.filename = "traderbot-sim-" + name + ".json"
        self.usd_balance = usd_balance
        self.btc_balance = btc_balance
        self.fee = fee
        self.persistent = persistent
        if self.persistent:
            try:
                self.load()
            except IOError:
                pass

    def buy(self, volume, price):
        logging.info("execute buy %f BTC @ %f on %s" %
                     (volume, price, self.name))
        self.usd_balance -= price * volume
        self.btc_balance += volume - volume * self.fee
        if self.persistent:
            self.save()

    def sell(self, volume, price):
        logging.info("execute sell %f BTC @ %f on %s" %
                     (volume, price, self.name))
        self.btc_balance -= volume
        self.usd_balance += price * volume - price * volume * self.fee
        if self.persistent:
            self.save()

    def load(self):
        data = json.load(open(self.filename, "r"))
        self.usd_balance = data["usd"]
        self.btc_balance = data["btc"]

    def save(self):
        data = {'usd': self.usd_balance, 'btc': self.btc_balance}
        json.dump(data, open(self.filename, "w"))

    def balance_total(self, price):
        return self.usd_balance + self.btc_balance * price

    def get_info(self):
        pass

class MockMarketRedis(MockMarket):
    def __init__(self, name, fee=0, usd_balance=500., btc_balance=15.):
        self.name = name
        self.redis_key = self.name
        self.usd_balance = usd_balance
        self.btc_balance = btc_balance
        self.fee = fee
        self.persistent = True
        url = urllib.parse.urlparse(config.rediscloud_url)
        self.redis = redis.Redis(host=url.hostname, port=url.port, password=url.password)

        if self.redis.get(self.redis_key) is None:
            # key is not set then save current balance
            self.save()
        else:
            # key is set then load existing balance
            self.load()
        
    def load(self):
        data = json.loads(self.redis.get(self.redis_key))
        self.usd_balance = data["usd"]
        self.btc_balance = data["btc"]

    def save(self):
        data = {'usd': self.usd_balance, 'btc': self.btc_balance}
        self.redis.set(self.redis_key, json.dumps(data))

class TraderBotSim(TraderBot):
    def __init__(self):
        self.kraken =   MockMarketRedis("kraken",   0.005, 500., 0.033) # 0.5% fee
        self.bitstamp = MockMarketRedis("bitstamp", 0.005, 500., 0.033) # 0.5% fee
        self.gdax =     MockMarketRedis("gdax",     0.005, 500., 0.033) # 0.5% fee
        self.bitfinex = MockMarketRedis("bitfinex", 0.005, 500., 0.033) # 0.5% fee
        self.gemini =   MockMarketRedis("gemini",   0.005, 500., 0.033) # 0.5% fee
        self.clients = {
            "KrakenUSD": self.kraken,
            "BitstampUSD": self.bitstamp,
            "GDAXUSD": self.gdax,
            "BitfinexUSD": self.bitfinex,
            "GeminiUSD": self.gemini,
        }
        self.profit_thresh = config.profit_thresh
        self.perc_thresh = config.perc_thresh
        self.trade_wait = 120
        self.last_trade = 0

    def total_balance(self, price):
        market_balances = [i.balance_total(
            price) for i in set(self.clients.values())]
        return sum(market_balances)

    def total_usd_balance(self):
        return sum([i.usd_balance for i in set(self.clients.values())])

    def total_btc_balance(self):
        return sum([i.btc_balance for i in set(self.clients.values())])

    def execute_trade(self, volume, kask, kbid,
                      weighted_buyprice, weighted_sellprice,
                      buyprice, sellprice):
        self.clients[kask].buy(volume, buyprice)
        self.clients[kbid].sell(volume, sellprice)

if __name__ == "__main__":
    t = TraderBotSim()
    print("Total BTC: %f" % t.total_btc_balance())
    print("Total USD: %f" % t.total_usd_balance())
