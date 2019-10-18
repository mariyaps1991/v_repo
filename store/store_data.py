"""
Maintain store and product information.
This is being used as database
"""

SHOP_NAME = "Nilgris"
SHOP_CODE = 12047

fruits = {'Apple': {'price': 120, 'stock': 3, "expiry_date": "09-2019"},
          'Banana': {'price': 40, 'stock': 2, "expiry_date": "12-2019"}}

stationary = {'Pen': {'price': 10.50, 'stock': 11},
              'Paper': {'price': 1.50, 'stock': 100},
              'Scissor': {'price': 15, 'stock': 6}}

grocery = {'Colgate': {'price': 30, 'stock': 1},
           'Soap': {'price': 5.50, 'stock': 10},
           'Honey': {'price': 350, 'stock': 2}}

data = [fruits, stationary, grocery]


store = {'name': 'Nilgris'}

