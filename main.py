import Coins
import Orders
import requests
import Trades

session = requests.session()

coins = list(Coins.get_coin_list())

fee_percent = 0.1

for i in coins:
    try:
        orders = Orders.get_orders(session,i)
        gap = Orders.top_orders(orders)[2]
        if gap > 1:
            trades = Trades.get_tardes(i,session)
            last = Trades.last_trade(trades)
            if last < 120:
               print(i , ' ' , gap)
    except:
        pass
