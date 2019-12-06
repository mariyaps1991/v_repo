from billing.cart import add_products_to_cart
#from store.store_data import data as store_data
from store.product_management import get_data
from calculator.basic_calculator import BasicCalculator
from utility.logger import Logging


class Pricing:

    def __init__(self, bill_data={}):
        if not bill_data:
            self.bill_data = {}
        self.bill_data = bill_data
        logging = Logging()
        self.logger = logging.get_logger()

    def get_bill(self):
        items = add_products_to_cart()
        self.get_bill_data(items)        # "Product, price "
        if not self.bill_data:
            self.logger.warning("Your cart is empty or not having available stocks")
            return None
        self.calculate_total()

    @staticmethod
    def show_bill_summary():
        pass

    @staticmethod
    def view_detailed_bill():
        pass

    def get_bill_data(self, cart_products):
        """
        This method is to print the bill copy
        :return: None
        """
        store_data = get_data()
        for cart_product in cart_products:
            item_found = False
            for category in store_data:
                for store_product, prod_data in category.items():
                    if cart_product == store_product:
                        print(f'Item {cart_product} is available in store')
                        item_found = True
                        self.bill_data.update({cart_product: prod_data['price']})

            if not item_found:
                self.logger.error(f'{cart_product} is not available in store')


    def calculate_total(self):
        """
        This is to provide the bill amount on the available items in cart
        :param data_dict: product and price combo
        :return: None
        """
        print("=" * 40)
        print("\tProduct {0:20} Price {0:10}".format(" "))
        print("-" * 40)

        price_list = self.bill_data .values()
        for product, price in self.bill_data .items():
            print(f"\t{product:20} {price:10}")
        print("=" * 40)
        amount = BasicCalculator.addition(price_list)
        print("Amount :: ", amount)


if __name__ == '__main__':
    obj = Pricing(bill_data={'Orange': 100, 'Knife': 25})
    obj.get_bill()