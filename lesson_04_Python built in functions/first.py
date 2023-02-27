"""
Create a list of different types of python objects, and print all the types. The one who gets the the most unique types wins respect points
"""

first_list = ["Vardas", 5, "15", 12, 2.56]





for item in first_list:
    print(type(item))


print(*first_list, sep="|")

