"""
Create a function that returns only strings with unique characters.
"""

text = input("Please enter the word: ")

def func_unique_characters(text):
    unique_characters = set(text)
    return unique_characters
print(func_unique_characters(text))