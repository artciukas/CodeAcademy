"""
create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)
padaryti badymu skaiciu...
"""



import random

random_number = random.randint(1, 10)


i = 1

while i < 4:
    entered_number = int(input("Gues number from 1 to 10 and write: "))
    if random_number == entered_number:
        print(f"You WIN: {entered_number} equel {random_number}")
        break
    else:
        print(f"Try again: {entered_number}")
        if entered_number < random_number:
            print("Random number is BIGER")
        else:
            print("Random number is SMALLER")
        i = i + 1
    
