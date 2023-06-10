#  MarketData
import kucoin.client
from kucoin.client import Market
from kucoin.client import User
from kucoin.client import Trade

api_key = "64280ed96a3d7300012bc3e7"
api_secret = "a19b04eb-d799-4375-9ac2-e123e46ba924"
api_passphrase = "TradeBot8448"
url = 'https://api.kucoin.com'

client_orders = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url=url)

# client_orders.cancel_all_orders()
# c = client_orders.get_all_stop_order_details()
# print(c)
# for i in c['items']:
#     print(i)


# client = Market(url=url)
#
user_data = User(api_key, api_secret, api_passphrase)


# c = client_orders.get_order_list()['items']

def cancel_buy_orders():
    buy_orders = client_orders.get_order_list(status='active', side='buy')['items']
    for i in buy_orders:
        # client_orders.cancel_order()
        # print(c)
        id = i['id']
        client_orders.cancel_order(id)


#
# print(a.get_account_list('ALPINE')[0]['balance'])
# for i in a.get_account_list():
#     print(i)




def put_sell_order(coin, target_price):
    volume = user_data.get_account_list(coin)[0]['balance']
    symbol = coin + '-USDT'
    b = client_orders.create_limit_order(symbol, 'sell', str(volume), str(target_price))
    print(b)


if __name__ == '__main__':
    # put_sell_order('CHMB',2)
    u = user_data.get_account_list()
    for i in u:
        if i['type'] == 'trade' and  i['balance'] != '0' and i['currency'] not in ('LMR','PIAS','USDT'):
            client_orders.create_market_order(i['currency']+'-USDT', 'sell', size=i['balance'])

            print(i)


    # a = client_orders.create_market_order('ARX-USDT','sell',size = '12154')
    # print(a)

