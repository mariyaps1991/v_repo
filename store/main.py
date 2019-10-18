import subprocess
from view import show_stocks
from product_management import add_products


def list_options():

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

    print(choice)

    if choice == 1:
        get_bill()
    elif choice == 2:
        show_stocks()
    elif choice == 3:
        add_products(category="Fruits")
    elif choice == 4:
        update_product_detail()
    elif choice == 5:
        remove_products()
    elif choice == 6:
        subprocess.call(['notepad', 'bill_summary.txt'])
        #show_bill_summary()
    elif choice == 7:
        view_detailed_bill()
    elif choice == 8:
        print("Closing the billing application")
        exit()
    else:
        print("Invalid choice. Please retry")


while True:
    list_options()
