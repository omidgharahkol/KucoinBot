#  MarketData
from kucoin.client import Market
from kucoin.client import User
from kucoin.client import Trade

api_key = "64280ed96a3d7300012bc3e7"
api_secret = "a19b04eb-d799-4375-9ac2-e123e46ba924"
api_passphrase = "TradeBot8448"
url = 'https://api.kucoin.com'

client_orders = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url=url)
c = client_orders.get_all_stop_order_details()
print(c)
for i in c['items']:
    print(i)


client = Market(url=url)

a = User(api_key, api_secret, api_passphrase)

print(a.get_base_fee())
