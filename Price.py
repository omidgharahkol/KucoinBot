import time
from kucoin.client import Market
import pandas as pd
import requests
import pandas
import datetime


def get_price_1min(symbol):
    end = datetime.datetime.now().timestamp()
    start = end - 120
    resp = Market().get_kline(symbol, '1min', startAt=int(start), endAt=int(end))[-1]

    open = float(resp[1])
    close = float(resp[2])
    high = float(resp[3])
    low = float(resp[4])

    # volume = list(map(float, resp['v']))
    # df = df.sort_values('timestamps', ascending=False).reset_index()
    #
    # rows, columns = df.shape

    PP = (high + low + close) / 3
    r1 = (2 * PP) - low
    s1 = (2 * PP) - high
    r2 = PP + (high - low)
    s2 = PP - (high - low)
    r3 = high + 2 * (PP - low)
    s3 = low - 2 * (high - PP)

    r1a = (r1 + r2) / 2
    r2a = (r1 + r3) / 2
    r3a = (r2 + r3) / 2

    s1a = (s1 + s2) / 2
    s2a = (s1 + s3) / 2
    s3a = (s2 + s3) / 2

    signals = {}
    signals['SELL'] = [r2a, (r1a + r2a) / 2, r1a]
    signals['BUY'] = [s3a, (s3a + s2a) / 2, (s3a + s1a) / 2, s2a, (s1a + s2a) / 2, s1a]

    return signals


def get_price_1hour(symbol):
    end = datetime.datetime.now().timestamp()
    start = end - 120 * 3600
    resp = Market().get_kline(symbol, '1hour', startAt=int(start), endAt=int(end))[-1]

    open = float(resp[1])
    close = float(resp[2])
    high = float(resp[3])
    low = float(resp[4])
    return high, low


if __name__ == '__main__':
    symbol = 'FTM-USDT'
    a = get_price_1min(symbol)
    b = get_price_1hour(symbol)
    print(a)
    print(b)
