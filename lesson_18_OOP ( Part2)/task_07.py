"""
Create a Person class which will have three properties:
    Name
    List of foods they like
    List of foods they hate
In this class, create the method taste():
    It will take in a food name as a string.
    Return {person_name} eats the {food_name}.
    If the food is in the person's like list, add 'and loves it!' to the end.
    If it is in the person's hate list, add 'and hates it!' to the end.
    If it is in neither list, simply add an exclamation mark to the end.
    p1 = Person("Sam", ["ice cream"], ["carrots"])
    p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
    p1.taste("cheese") ➞ "Sam eats the cheese!"
    p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"
"""

class Person:
    def __init__(self, name, food_like, food_hate) -> None:
        self.name = name
        self.food_like = food_like
        self.food_hate = food_hate

    def taste(self, food):
        if food in self.food_like:
            answer = "Love"
            return f"{self.name} eats the {food} and {answer}"
        if food in self.food_hate:
            answer = "Hate"
            return f"{self.name} eats the {food} and {answer}"
        return f"{self.name} eats the {food} and {answer}"




p1 = Person("Sam", food_like= ["ice cream"], food_hate=["carrots"])
print(p1.taste("ice cream"))