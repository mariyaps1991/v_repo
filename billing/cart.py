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
    elif args:
        for product_name in args:
            cart.append(product_name)

    display_cart_items()
    print("Items added successfully")
    return cart


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



def main():
    """
    Main function to add and display cart information
    :return: None
    """
    add_products_to_cart()


if __name__ == '__main__':
    main()
