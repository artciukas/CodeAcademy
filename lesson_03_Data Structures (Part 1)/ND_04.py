"""
Write a python program that concatenates all strings in the list (all items are strings, create a list yourself)
"""

my_list = ["Tomas", "Karolis", "Dovydas"]
x = ""
for word in my_list:
    x = x + word
    print(x)

print(x)