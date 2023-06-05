def add_price(price, add_number):
    number, decimal = str(float(price)).split('.')
    if decimal == '0':
        new_price = price + add_number
        return float(new_price)
    else:
        count_decimal = len(decimal)

        new_price = price + add_number / (10 ** count_decimal)
        return new_price


if __name__ == '__main__':
    c = add_price(10.602, 2)
    print(c)
