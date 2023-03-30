"""
Write a class called CoffeeShop, which has three instance variables:

name : a string (basically, of the shop)
menu : a list of items (of dict type), with each item containing the item (name of the item), type (whether a food or a drink) and price.
orders : an empty list
and seven methods:

add_order: adds the name of the item to the end of the orders list if it exists on the menu, o
therwise, return "This item is currently unavailable!"

fulfill_order: if the orders list is not empty, return "The {item} is ready!". If the orders list is empty, return "All orders have been fulfilled!"

list_orders: returns the item names of the orders taken, otherwise, an empty list.

due_amount: returns the total amount due for the orders taken.

cheapest_item: returns the name of the cheapest item on the menu.

drinks_only: returns only the item names of type drink from the menu.

food_only: returns only the item names of type food from the menu.

IMPORTANT: Orders are fulfilled in a FIFO (first-in, first-out) order. Examples:


"""

class CoffeeShop:
    def __init__(self, name: str, meniu: dict, orders: list) -> None:
        self.name = name
        self.meniu = meniu
        self.orders = orders



    def add_order(self):
        for item in orders:
            if item is self.meniu.keys():
                print({item})
            else:
                print('no')
           

    def fulfill_order(self):
        if len(self.orders) == 0:
            print('This item is currently unavailable!')
        else:
            for item in self.orders:
                print(f'The {item} is ready!')


    def list_orders(self):
        if len(self.orders) == 0:
            print(self.orders)
        else:
            print(self.orders)
    
    def due_amount(self):
        for p_id, p_info in self.meniu.items():
            print("\nFood type:", p_id)
    
            for key in p_info:
               print(key)
               
            


meniu = {
"foods": {"orange juice" : "3.15", "lemonade": "2.15"  },
"drinks": {"tuna sandwich": "3.50", "ham and cheese sandwich": "4.45"}
        }

orders = ['tuna sandwich', "ham and cheese sandwich"]

first_order = CoffeeShop('Cili', meniu, orders)
first_order.add_order()
# first_order.fulfill_order()
# first_order.list_orders()
# first_order.due_amount()

# for food_type in meniu.items():
#     print(food_type)
#     # for key in food_type:
#         # print(key)







