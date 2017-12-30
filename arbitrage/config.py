import os

# This is imported into the arbitrer and used to import the relevent modules from public_markets.
markets = os.environ["MARKETS"].split(",")

# This is imported into the tradeBot and used to import the relevent modules from private_markets.
clients = os.environ["CLIENTS"].split(",")

# observers if any
# This is imported into the arbitrer and used to import the relevent modules.
# ["Logger", "DetailedLogger", "TraderBot", "TraderBotSim", "HistoryDumper", "Emailer"]
observers = os.environ["OBSERVERS"].split(",")

market_expiration_time = 120  # in seconds: 2 minutes

refresh_rate = int(os.environ["REFRESH_RATE"])

#### Trader Bot Config
# Access to Private APIs

paymium_username = "FIXME"
paymium_password = "FIXME"
paymium_address = "FIXME"  # to deposit btc from markets / wallets

bitstamp_username = "FIXME"
bitstamp_password = "FIXME"

rediscloud_url = os.environ["REDISCLOUD_URL"]
# SafeGuards
max_tx_volume = 10  # in BTC
min_tx_volume = float(os.environ["MIN_TX_VOLUME"]) # in BTC
balance_margin = 0.05  # 5%
profit_thresh = float(os.environ["PROFIT_THRESH"]) # in USD
perc_thresh = float(os.environ["PERC_THRESH"]) # in %

#### Emailer Observer Config
smtp_host = 'FIXME'
smtp_login = 'FIXME'
smtp_passwd = 'FIXME'
smtp_from = 'FIXME'
smtp_to = 'FIXME'

#### XMPP Observer
xmpp_jid = "FROM@jabber.org"
xmpp_password = "FIXME"
xmpp_to = "TO@jabber.org"
