from arbitrage import config
from arbitrage.private_markets.market import Market, TradeException
import ccxt


class PrivateKrakenUSD(Market):
    def __init__(self):
        self.ccxt_market = ccxt.kraken({'apiKey': config.kraken_api_key,
                                        'secret': config.kraken_secret})
        self.currency = "USD"
        super().__init__()
