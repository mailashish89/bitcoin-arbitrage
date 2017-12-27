from arbitrage.public_markets._bitstamp_ccxt import BitstampCcxt

class BitstampUSDCcxt(BitstampCcxt):
    def __init__(self):
        super().__init__("USD")

if __name__ == "__main__":
    market = BitstampUSDCcxt()
    market.update_depth()
    print(market.get_ticker())
 