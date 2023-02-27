"""
Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.
"""

name = str(input("Please enter your NAME: "))
surname = str(input("Please enter your SURNAME: "))
age = int(input("Please enter your AGE: "))

if age >= 21:
    print(f'{name},{surname} entered to CASINO')
else:
    print(f"Sorry!!!! {name} not allow to CASINO")