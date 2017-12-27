from arbitrage.public_markets.market_ccxt import MarketCcxt
import ccxt

class KrakenCcxt(MarketCcxt):
    def __init__(self, currency):
        super().__init__(currency)
        self.update_rate = 30
        self.ccxt_market = ccxt.kraken()
