import requests


def get_coin_list():
    url = "https://api.kucoin.com/api/v2/symbols"
    resp = requests.get(url).json()

    for i in resp['data']:
        if i['quoteCurrency'] == 'USDT':
            yield i['symbol']


if __name__ == "__main__":
    print(list(get_coin_list()))
