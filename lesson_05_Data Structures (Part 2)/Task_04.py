"""
Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary
"""
dictionary = {}
dictionary["name"] = str(input("Please write name: "))
dictionary["surname"] = str(input("Please enter surname: "))
dictionary["age"] = int(input("Please enter your age: "))

print(dictionary)