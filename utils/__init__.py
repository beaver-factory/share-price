

def calculate_price_change(current_price, last_price):
    diff = current_price-last_price

    return (diff/last_price)*100


def calculate_absolute_change(current_price, last_price):
    return current_price-last_price
