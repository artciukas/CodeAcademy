
# Lambdas section:
"""
Write a Python program to find if a given string starts with a given character using Lambda. Sample Output: True False
"""
# task_01
# starts_with = lambda x: True if x.startswith('A') else False
# print(starts_with('Arturas'))
# starts_with = lambda x: True if x.startswith('B') else False
# print(starts_with('Tomas'))

# task_02
"""
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and print the result.
"""
# adds_fifteen = (lambda number: number * 15)(3)
# print(adds_fifteen)
# multiplay_x_y = (lambda x, y: x * y)(5,6)
# print(multiplay_x_y)

# task_03
"""
Write a Python program to add two given lists using map and lambda.
"""
# list_one = ['a', 'b', 'c']
# list_two = ['x', 'w', 'z']
# map_list = map(lambda x, y: x + y, list_one, list_two)
# print(list(map_list))
# task_04
"""
Write a Python program to square and cube every number in a given list of integers using Lambda
"""
number_list = [1, 3, 5]
square_cube = map(lambda x: (x**2, x**3), number_list)
print(type(square_cube))
print(square_cube)

# task_05
"""
Write a Python program to extract year, month, date and time using Lambda. Sample Output: 2020-01-15 09:03:32.744178 2020 1 15 09:03:32.744178
"""
# import datetime
# current_time = datetime.datetime.now()
# print(current_time)
# year = lambda x: x.year
# print(year(current_time))
# month = lambda x: x.month
# print(month(current_time))
# day = lambda y: y.day
# print(day(current_time))
# time = lambda t: t.strftime("%H:%M:%S")
# print(time(current_time))
