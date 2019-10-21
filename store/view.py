import store_data


def show_stocks(category=None):
    stocks = store_data.data
    print("-" * 50)
    print(f"{'Product':15} {'Price':6} {'Stock':5} {'Expiry Date':12}")
    print("=" * 50)
    if category == 'fruits':
        stocks = [stocks[0]]
    elif category == 'stationary':
        stocks = [stocks[1]]
    elif category == 'grocery':
        stocks = [stocks[2]]

    #print(stocks)

    for stock_type in stocks:       # list
        for product, prod_data in stock_type.items():
            print(f"{product:15} {prod_data['price']:6} {prod_data['stock']:5} {prod_data.get('expiry_date', 'None'):12}")
        print("-"*50)


if __name__ == '__main__':
    show_stocks('grocery')