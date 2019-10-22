from store_data import data as store_data
from view import show_stocks


global fruits


def update_product_detail():
    pass


def add_products_to_store(*args):
    category = input("Enter the product category(fruits, grocery, stationary): ")
    item = {}
    price = 0

    if not args:
        product = input("Enter the product name: ")
        price = float(input(f"Enter price of {product}: "))
        quantity = int(input(f"Enter the quantity of {product}: "))
        expiry_date = input(f"Enter the expiry date of {product}: ")
        product_data = {'price': price, 'stock': quantity, 'expiry_date': expiry_date}
        item = {product: product_data}
    else:
        for product in args:
            value = float(input(f"Enter price of {product}: "))
            quantity = int(input(f"Enter the quantity of {product}: "))
            expiry_date = input(f"Enter the expiry date of {product}: ")
            product_data = {'price': value, 'stock': quantity, 'expiry_date': expiry_date}
            one_product = {product: product_data}
            item.update(one_product)
            price = price + value

    if category == 'fruits':
        fruits = store_data[0]
        fruits.update(item)
    if category == 'stationary':
        stationary = store_data[2]
        stationary.update(item)
    if category == 'grocery':
        grocery = store_data[1]
        grocery.update(item)

    show_stocks(category)
    print('Price: ', price)
    return price


def validate_product_expiry():
    alert_product_expiry()


def alert_product_unavailability():
    pass


def alert_product_expiry():
    pass


if __name__ == '__main__':
    add_products_to_store('Orange', 'Gova', 'Pomo')
