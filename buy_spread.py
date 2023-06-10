import Coins
import Kucoin
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
        if gap > 0.3 and gap < 0.7:
            trades = Trades.get_tardes(i, session)
            last = Trades.last_trade(trades)
            valoume = Trades.trades_volume(trades)
            if last < 60:
                print(i, ' ', gap, ' ', valoume, Utility.add_price(min, 0))
                with open('Spread.txt', 'a') as the_file:
                    a = Kucoin.client_orders.create_limit_order(i, 'buy', str(int(valoume)),
                                                                str(Utility.add_price(min, 0)))
                    print(a)
                    the_file.write('{},{},{}\n'.format(i, Utility.add_price(max, -0), valoume))

    except Exception as e:
        print(str(e))

    # c += 1
    # print(c)

with open('Spread.txt', 'a') as the_file:
    the_file.write('EndSpread')
