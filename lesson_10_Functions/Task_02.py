"""
Create a function that adds a string ending to each member in a list.
"""
from typing import Union, List

user_input = input("Please enter Name add to the list")

my_list = ["1", "2", "3", "4"]

def add_to_the_list(user_input, my_list):
    created_list = []
    for item in my_list: 
        created_list.append(item + user_input)
    
    return created_list

a = add_to_the_list(user_input, my_list)
print(a)