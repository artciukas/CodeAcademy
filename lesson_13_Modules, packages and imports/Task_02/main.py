"""
Create a program with 3 different modules:
first, to do basic tasks with strings
second, basic tasks with lists.
third, basic tasks with numbers
"""

import first_module_greeting
import second_module_list as find_in_list
from thitd_module_sum_numbers import sum_number


print(first_module_greeting.greeting(input("Please write a name: ")))
print(find_in_list.check_in_list(3))
print(sum_number(first_number = 5, second_number = 5))



