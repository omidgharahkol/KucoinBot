import requests

import requests
import numpy as np





def get_orders(session,symbol):
    url = 'https://api.kucoin.com/api/v1/market/orderbook/level2_100?symbol=%s' % symbol
    orders = session.get(url).json()['data']
    return orders



def gap_orders(orders):
    shape = len(orders['bids'])
    bids = []
    asks = []
    for i in range(shape):
        bids.append(float(orders['bids'][i][0]))
        asks.append(float(orders['asks'][i][0]))


    diff_asks = np.diff(asks)
    avg_asks = 4 * np.mean(diff_asks)
    diff_bids = np.diff(bids)
    avg_bids = 4 * np.mean(diff_bids)
    for i in range(shape - 1):
        if diff_bids[i] < avg_bids:
            print('buy : ', bids[i + 1])
        if diff_asks[i] > avg_asks:
            print('ask : ', asks[i + 1])


def top_orders(orders):
    ask_price = float(orders['asks'][0][0])
    bid_price = float(orders['bids'][0][0])

    return ask_price, bid_price , 100*(ask_price - bid_price)/bid_price


if __name__ == '__main__':
    symbol = 'ALPINE-USDT'
    session = requests.session()
    orders = get_orders(session,symbol)
    gap_orders(orders)
    v = top_orders(orders)[0]
    print(v)
    number , decimal = str(v).split('.')
    b = number +'.'+str(int(decimal) + 5)
    print(float(b))


