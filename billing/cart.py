from store.store_data import data


cart = []


def add_products_to_cart(*args):
    """
    This method is to add product to cart
    :return: None
    """
    if not args:
        done_adding_products = False
        while not done_adding_products:
            product_name = input("Enter the product name: ")
            cart.append(product_name)
            done_adding_products = input("Done adding products to cart? Default 'n' (y/n): ")
            if done_adding_products == 'y' or done_adding_products == 'yes':
                done_adding_products = True
            else:
                done_adding_products = False
    else:
        for product_name in args:
            cart.append(product_name)

    display_cart_items()

    print("Items added successfully")


def display_cart_items():
    """
    Display the products in cart
    :return: None
    """
    print("=" * 40)
    print("You have added below products to your cart.")
    #print(products)
    for sno, product in enumerate(cart, 1):
        print(str(sno) + ". " + product)
    print("=" * 40, "\n")


def print_bill():
    """
    This method is to print the bill copy
    :return: None
    """
    products_to_bill = {}
    for cart_product in cart:
        for category in data:
            for product, prod_data in category.items():
                if cart_product == product:
                    print(f'Item {cart_product} found')

    print("\tProduct {0:20} Price {0:10}".format(" "))
    print("-" * 40)
    """
    for product, price in products_to_bill.items():
        if product in products:
            print(f"\t{product:20} {price:10}")
    print("=" * 40)
    """


def main():
    """
    Main function to add and display cart information
    :return: None
    """
    add_products_to_cart('Orange')
    print_bill()

main()
