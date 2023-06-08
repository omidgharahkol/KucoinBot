import Coins
import KucoinClient
import Orders
import requests
import Trades
import Utility

session = requests.session()

coins = list(Coins.get_coin_list())

fee_percent = 0.1

c = 0

for i in coins:
    try:
        orders = Orders.get_orders(session, i)
        max, min, gap = Orders.top_orders(orders)
        if gap > 1:
            trades = Trades.get_tardes(i, session)
            last = Trades.last_trade(trades)
            valoume = Trades.trades_volume(trades)
            if last < 120:
                print(i, ' ', gap, ' ', valoume  , Utility.add_price(min , 2))
                with open('Spread.txt', 'a') as the_file:
                    a = Kucoin.client_orders.create_limit_order(i, 'buy', str(int(valoume)), str(Utility.add_price(min , 2)))
                    print(a)
                    the_file.write('{},{},{}\n'.format(i, Utility.add_price(max, -2), valoume))

    except Exception as e:
        print(str(e))

    # c += 1
    # print(c)

with open('Spread.txt', 'a') as the_file:
    the_file.write('EndSpread')
