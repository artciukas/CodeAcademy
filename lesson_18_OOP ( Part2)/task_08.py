"""
Create a class Smoothie and do the following:
Create an instance attribute called ingredients.
Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. 
    If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". 
    Remember to change "-berries" to "-berry". See the examples below.
Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call 
all methods you implemented.

"""

class Smoothie:
    price = {'stroberries': 1, 'banana': 0.5, 'mango': 2, 'apple':0.44}

    def __init__(self, ingredients: list) -> None:
        self.ingredients = ingredients

    def get_cost(self):
        self.total_price = 0
        for self.ingredient in self.ingredients:
            ingridient_price = self.price.get(self.ingredient)
            self.total_price += ingridient_price
        return self.total_price
    
    def get_price(self):
        return round(self.total_price * 1.5, 2)
    
    def get_name(self):
        self.ingredients.sort()
        
        





coctail = Smoothie(["stroberries", "banana", 'apple'])
print(coctail.get_cost())
print(coctail.get_price())
coctail.get_name()
# coctail_one = Smoothie(ingredient = ['lime', 'banana'])
# print(coctail_one)