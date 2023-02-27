"""
Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself)
"""

my_list = [2.5, 3, 8, 9, 12]
b = 1

for number in my_list:
    b = number * b
    
    print(b)

print(f"Sandauga yra: {b}")