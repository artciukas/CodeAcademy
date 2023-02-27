"""
Write a python program that asks user to enter 3 integers and find the highest value entered.
"""

number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))
number3 = int(input("Please enter third number: "))

number_list = [number1, number2, number3]

print(max(number_list))


