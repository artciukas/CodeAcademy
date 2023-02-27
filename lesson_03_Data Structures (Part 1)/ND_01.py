'''
Write a python program that sums up all items in the list (all items are integers or floats in list, create a list yourself)
'''

my_list = [5, 8, 6, 9, 1]
x = 0

for number in my_list:
    x = number + x
    print(x)


print(f"Sandauga yra: {x}")

