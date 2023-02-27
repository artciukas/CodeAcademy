"""
Write a program to remove the duplicate in a list
"""

numbers = [12, 15, 15, 16, 5, 100, 16]

uniquies = []

for number in numbers:
    if number not in uniquies:
        uniquies.append(number)
print(uniquies)