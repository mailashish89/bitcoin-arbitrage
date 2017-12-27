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

paymium_api_key = "FIXME"
paymium_secret = "FIXME"

bitstamp_api_key = "FIXME"
bitstamp_secret = "FIXME"

# SafeGuards
max_tx_volume = 10  # in BTC
min_tx_volume = 1  # in BTC
balance_margin = 0.05  # 5%
profit_thresh = 1  # in EUR
perc_thresh = 2  # in %

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
