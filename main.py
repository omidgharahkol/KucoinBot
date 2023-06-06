import Coins
import Orders
import requests
import Trades

session = requests.session()

coins = list(Coins.get_coin_list())

fee_percent = 0.1

c = 0

for i in coins:
    try:
        orders = Orders.get_orders(session,i)
        gap = Orders.top_orders(orders)
        if gap > 1:
            trades = Trades.get_tardes(i,session)
            last = Trades.last_trade(trades)
            if last < 120:
               print(i , ' ' , gap[2])
               with open('file.txt', 'a') as the_file:
                   the_file.write('{},{}\n'.format(i,gap[1]))

    except:
        pass

    c += 1
    print(c)

with open('file.txt', 'a') as the_file:
    the_file.write('EndSpread')