"""
allow user to enter two numbers, print out which one is higher than the other, or are they equal?
"""

first_number = int(input("Please enter first number: "))
second_number = int(input("Please enter second number: "))

if first_number > second_number:
    print(f"{first_number} is bigger then {second_number}")
elif first_number < second_number: 
    print(f"{first_number} is smaller then {second_number}")
else:
    print(f"{first_number} is eqel {second_number}")


