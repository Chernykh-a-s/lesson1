def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

my_price = format_price(56.24)
print(my_price)