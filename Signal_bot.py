import datetime
import time

import numpy as np

import Price

import requests
import Orders

session = requests.session()
symbol = 'FTM-USDT'



def r_and_s_formula(symbol, Orders_data):
    # symbol = 'USDTTMN'
    # session = requests.session()

    data = {}
    data['buy'] = []
    data['sell'] = []

    b_1min = Price.get_price_1min(symbol)
    b_1hour = Price.get_price_1hour(symbol)
    a = Orders.top_orders(Orders_data)
    sells = b_1min['SELL']
    buys = b_1min['BUY']
    order_gap = (a[0] - a[1]) / a[0]
    fee = 0.001
    # print(b_1min)
    # print('1 Hour : ' , b_1hour)
    # print('orders : ',a)
    # print('orders gap : ' ,a[0] - a[1] , ' ' , order_gap)
    # print('fee : ',fee)

    if buys[0] > a[1] and buys[1] > a[1]:
        if order_gap > 2 * fee:
            # print('buy : ',a[1] + 2)
            data['buy'].append(a[1])
    else:
        # print('buy : ', buys[0])
        # print('buy : ', buys[1])
        data['buy'].append(buys[0])
        data['buy'].append(buys[1])

    if buys[0] < b_1hour[1] and buys[1] < b_1hour[1]:
        pass
    else:
        data['buy'].append(b_1hour[1])
        # print('buy : ',b_1hour[1])

    # sell
    if sells[0] < a[0] and sells[1] < a[0]:
        if order_gap > 2 * fee:
            data['sell'].append(a[0])
            # print('sell : ', a[0] - 2)
    else:
        # print('sell : ', sells[0])
        # print('sell : ', sells[1])
        # print('sell : ', sells[2])
        data['sell'].append(sells[0])
        data['sell'].append(sells[1])
        data['sell'].append(sells[2])

    if sells[0] > b_1hour[0] and sells[1] > b_1hour[0]:
        pass
    else:
        data['sell'].append(b_1hour[0])
        # print('sell : ', b_1hour[0])

    return data


def get_s_and_r_from_orders(Orders_data):
    shape = len(Orders_data['bids'])
    bids = []
    asks = []
    for i in range(shape):
        bids.append(float(Orders_data['bids'][i][0]))
        asks.append(float(Orders_data['asks'][i][0]))

    diff_asks = np.diff(asks)
    avg_asks = 4 * np.mean(diff_asks)
    diff_bids = np.diff(bids)
    avg_bids = 4 * np.mean(diff_bids)

    data = {}
    data['buy'] = []
    data['sell'] = []
    for i in range(shape - 1):
        if diff_bids[i] < avg_bids:
            data['buy'].append(bids[i + 1])
            # print('buy : ', bids[i + 1] + 2)

            # w.put_order(symbol, 'BUY', bids[i + 1] + 2, 7, session)
        if diff_asks[i] > avg_asks:
            data['sell'].append(asks[i + 1])
            # print('sell : ', asks[i + 1] - 2)
    return data


if __name__ == '__main__':
    session = requests.session()
    symbol = 'FTM-USDT'

    Orders_data = Orders.get_orders(session, symbol)

    data = r_and_s_formula(symbol,Orders_data)
    data2 = get_s_and_r_from_orders(Orders_data)
    buys = data['buy'] + data2['buy']
    sells = data['sell'] + data2['sell']
    sells.sort(reverse=False)
    buys.sort(reverse=True)
    # print(buys)
    # print(sells)
    max_buy = buys[0]
    min_sells = sells[0]
    r = ((min_sells - max_buy) / max_buy)
    fee = 0.001
    print(r)
    if r > 2 * fee:
        print(buys)
        print(sells)
