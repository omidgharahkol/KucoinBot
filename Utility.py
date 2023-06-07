def add_price(price, add_number):
    len_first = len(str(price))
    print(len_first)
    number, decimal = str(float(price)).split('.')
    if decimal == '0':
        new_price = price + add_number
        new_price = str(new_price)[:len_first]
        return float(new_price)
    else:
        count_decimal = len(decimal)

        new_price = price + add_number / (10 ** count_decimal)
        new_price = float(str(new_price)[:len_first])
        return new_price


if __name__ == '__main__':
    c = add_price(0.011192, -3)
    print(c)
