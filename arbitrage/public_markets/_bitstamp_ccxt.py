from arbitrage.public_markets.market_ccxt import MarketCcxt
import ccxt

class BitstampCcxt(MarketCcxt):
    def __init__(self, currency):
        super().__init__(currency)
        self.update_rate = 20 #TODO set this to something sensible
        self.ccxt_market = ccxt.bitstamp()
