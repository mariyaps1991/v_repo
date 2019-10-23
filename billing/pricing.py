from billing.cart import add_products_to_cart
#from store.store_data import data as store_data
from billing import data


def get_bill():
    print(data)
    exit()
    items = add_products_to_cart()
    bill_data = get_bill_data(items)        # "Product, price "
    if not bill_data:
        print("Your cart is empty or not having available stocks")
        return None
    calculate_total(bill_data)


def get_bill_data(cart_products):
    """
    This method is to print the bill copy
    :return: None
    """
    bill_data = {}
    for cart_product in cart_products:
        item_found = False
        for category in store_data:
            for store_product, prod_data in category.items():
                if cart_product == store_product:
                    print(f'Item {cart_product} is available in store')
                    item_found = True
                    bill_data.update({cart_product: prod_data['price']})

        if not item_found:
            print(f'{cart_product} is not available in store')

    return bill_data


def calculate_total(data_dict):
    """
    This is to provide the bill amount on the available items in cart
    :param data_dict: product and price combo
    :return: None
    """
    print("=" * 40)
    print("\tProduct {0:20} Price {0:10}".format(" "))
    print("-" * 40)

    for product, price in data_dict.items():
        print(f"\t{product:20} {price:10}")
    print("=" * 40)


if __name__ == '__main__':
    get_bill()