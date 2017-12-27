from arbitrage import config
from arbitrage.private_markets.market import Market
import ccxt


class PrivatePaymium(Market):
    def __init__(self):
        super().__init__()
        self.ccxt_market = ccxt.paymium({'apiKey': config.paymium_api_key,
                                         'secret': config.paymium_secret})
        self.currency = "EUR"