from arbitrage.public_markets._kraken_ccxt import KrakenCcxt

class KrakenUSDCcxt(KrakenCcxt):
    def __init__(self):
        super().__init__("USD")
        
if __name__ == "__main__":
    market = KrakenUSDCcxt()
    market.update_depth()
    print(market.get_ticker())
