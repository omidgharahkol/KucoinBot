import Kucoin

last_value = ''

while last_value != 'EndSpread':
    with open("Spread.txt") as file_in:
        lines = []
        for line in file_in:
            if line == 'EndSpread':
                last_value = 'EndSpread'
                break
            else:
                symbol, target_price, volume = line.strip('\n').split(',')
                coin = symbol.split('-')[0]
                try:
                    Kucoin.put_sell_order(coin, target_price)
                except:
                    pass

Kucoin.cancel_buy_orders()
file_to_delete = open("Spread.txt", 'w')
file_to_delete.close()
