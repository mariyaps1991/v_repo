import subprocess
from view import show_stocks
from product_management import add_products_to_store, update_product_detail, remove_products
from billing.pricing import Pricing
#from billing.pricing import get_bill, show_bill_summary, view_detailed_bill
from utility.logger import Logging


class Menu:

    def __init__(self):
        logging = Logging()
        self.logger = logging.get_logger()

    def list_options(self):

        choice = int(input("""
                ============
                    MENU
                ============
                
                1. Bill desk
                2. Show stocks
                3. Add products to store
                4. Update product information
                5. Remove products
                6. List Bill Summary
                7. View detailed bill information
                8. Exit
                
                Enter your choice: 
                """))

        pr = Pricing()
        action = {1: pr.get_bill,
                  2: show_stocks,
                  3: add_products_to_store,
                  4: update_product_detail,
                  5: remove_products,
                  6: pr.show_bill_summary,
                  7: pr.view_detailed_bill,
                  8: exit
                  }

        execute = None

        try:
            execute = action[choice]
        except KeyError:
            self.logger.error("Invalid option. Please select correct one from the menu.")

        if execute:
            execute()

    def run(self):
        while True:
            self.list_options()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
    print(dir(menu))
