import store_data


def show_stocks():
    stocks = store_data.data
    print("-" * 50)
    print(f"{'Product':15} {'Price':6} {'Stock':5} {'Expiry Date':12}")
    print("=" * 50)
    for stock_type in stocks:
        for product, prod_data in stock_type.items():
            print(f"{product:15} {prod_data['price']:6} {prod_data['stock']:5} {prod_data.get('expiry_date', 'None'):12}")
        print("-"*50)


if __name__ == '__main__':
    show_stocks()