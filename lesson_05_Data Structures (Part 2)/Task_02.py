"""
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x): 
You can use input to receive the number. Example: n= 5 , output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

dictionary = {}
input_a = int(input("Please write number n: "))

for n_value in range(0, input_a + 1):
    dictionary[n_value] = n_value * n_value

print(dictionary)
