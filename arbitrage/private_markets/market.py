import logging
from arbitrage.fiatconverter import FiatConverter
import ccxt

class TradeException(Exception):
    pass

class Market:
    def __init__(self):
        self.name = self.__class__.__name__
        self.btc_balance = 0.
        self.eur_balance = 0.
        self.usd_balance = 0.
        self.fc = FiatConverter()
        #self.currency = 
        #self.ccxt_market = 
        self.get_info() # updates balances

    def __str__(self):
        return "%s: %s" % (self.name, str({"btc_balance": self.btc_balance,
                                           "eur_balance": self.eur_balance,
                                           "usd_balance": self.usd_balance}))

    def buy(self, amount, price):
        """Orders are always priced in USD"""
        local_currency_price = self.fc.convert(price, "USD", self.currency)
        logging.info("Buy %f BTC at %f %s (%f USD) @%s" % (amount,
                     local_currency_price, self.currency, price, self.name))
        self._buy(amount, local_currency_price)


    def sell(self, amount, price):
        """Orders are always priced in USD"""
        local_currency_price = self.fc.convert(price, "USD", self.currency)
        logging.info("Sell %f BTC at %f %s (%f USD) @%s" % (amount,
                     local_currency_price, self.currency, price, self.name))
        self._sell(amount, local_currency_price)

    def _buy(self, amount, price):
        #TODO deal with errors
        self.ccxt_market.create_limit_buy_order("BTC/USD",amount,price)

    def _sell(self, amount, price):
        #TODO deal with errors
        self.ccxt_market.create_market_sell_order("BTC/USD",amount)

    def deposit(self):
        raise NotImplementedError("%s.sell(self, amount, price)" % self.name)

    def withdraw(self, amount, address):
        raise NotImplementedError("%s.sell(self, amount, price)" % self.name)
        
    def get_info(self):
        """Get balance"""
        #This just gets the balance available for trading, not the total balance.
        self.btc_balance = float(self.ccxt_market.fetch_balance()["free"].get("BTC"))
        self.usd_balance = float(self.ccxt_market.fetch_balance()["free"].get("USD"))
        self.eur_balance = float(self.ccxt_market.fetch_balance()["free"].get("EUR"))
