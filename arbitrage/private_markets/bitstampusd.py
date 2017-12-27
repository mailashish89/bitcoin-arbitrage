from arbitrage import config
from arbitrage.private_markets.market import Market, TradeException
import ccxt


class PrivateBitstampUSD(Market):
    def __init__(self):
        super().__init__()
        self.ccxt_market = ccxt.bitstamp({'apiKey': config.bitstamp_api_key,
                                          'secret': config.bitstamp_secret})
        self.currency = "USD"
