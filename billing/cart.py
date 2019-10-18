
products = []
products_to_bill = {'Pen': 5, 'Pencil': 2, 'Colgate': 10}


def add_items():
    """
    This method is to add product to cart
    :return: None
    """
    product_name = input('Enter the product name: ')
    products.append(product_name)
    print("Items added successfully")


def display_items():
    """
    Display the products in cart
    :return: None
    """
    print("=" * 40)
    print("You have added below products to your cart.")
    #print(products)
    for sno, product in enumerate(products, 1):
        print(str(sno) + ". " + product)
    print("=" * 40, "\n")


def print_bill():
    """
    This method is to print the bill copy
    :return: None
    """
    print("\tProduct {0:20} Price {0:10}".format(" "))
    print("-" * 40)
    for product, price in products_to_bill.items():
        if product in products:
            print(f"\t{product:20} {price:10}")
    print("=" * 40)


def main():
    """
    Main function to add and display cart information
    :return: None
    """
    want_to_proceed = True
    while want_to_proceed:
        add_items()
        want_to_exit = input('Done adding product to the cart(default "n")? (y/n)')
        if want_to_exit == 'y':
            want_to_proceed = False

    display_items()
    print_bill()

main()
