from store_data import data as store_data
from view import show_stocks


def update_product_detail():
    pass


def add_products(category=None, product=None, price=None, quantity=None, expiry_date=None):
    category = input("Enter the product category(fruits, grocery, stationary): ")
    product = input("Enter the product name: ")
    price = float(input(f"Enter price of {product}: "))
    quantity = int(input(f"Enter the quantity of {product}: "))
    expiry_date = input(f"Enter the expiry date of {product}: ")
    product_data = {'price': price, 'stock': quantity, 'expiry_date': expiry_date}
    item = {product: product_data}
    if category == 'fruits':
        fruits = store_data[0]
        fruits.update(item)
    if category == 'stationary':
        stationary = store_data[2]
        stationary.update(item)
    if category == 'grocery':
        grocery = store_data[1]
        grocery.update(item)

    show_stocks()
    return price


def validate_product_expiry():
    alert_product_expiry()


def alert_product_unavailability():
    pass


def alert_product_expiry():
    pass

add_products()