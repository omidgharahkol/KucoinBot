import time

import requests
import datetime
import numpy as np


# open.append(float(i[1]))
# close.append(float(i[2]))
# high.append(float(i[3]))
# low.append(float(i[4]))
# volume.append(float(i[5]))
# turnover.append(float(i[6]))


def get_tardes(symbol, session):
    url = "https://api.kucoin.com/api/v1/market/histories?symbol=%s" % (symbol)

    resp = session.get(url).json()['data']
    return resp


def trades_volume(trades):
    sum_volume = 0
    lenght = len(trades)
    size = 0
    for i in range(lenght):
        sum_volume += float(trades[i]['price']) * float(trades[i]['size'])
        size += float(trades[i]['size'])

    return sum_volume / lenght


def last_trade(trades):
    c = 1000000000

    last_trade = trades[-1]['time'] / c

    diff = time.time() - last_trade

    return diff

    # print(time.time())
    # print(datetime.datetime.fromtimestamp(last_trade))
    # print(datetime.datetime.fromtimestamp(time.time()))

    # times = []
    # for i in resp:
    #     times.append(i['time'])
    #
    # diff_times = np.diff(times)
    #
    # avg_diff_times = np.mean(diff_times) / c
    # print(avg_diff_times)


if __name__ == '__main__':
    symbol = 'AXS3S-USDT'
    session = requests.session()
    a = get_tardes(symbol, session)
    b = trades_volume(a)
    c = last_trade(a)
    print(b)
    # print(a)
