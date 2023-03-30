"""
# Create a console application wich takes a sentece of at least 10 words.
# - print words in reverse order.
# - calculate how many items are in thw sentece. Do not include empty spaces.
"""

sentente =  input("Please enter sentence at least 10 rords: ").split(" ")
print(sentente)
sorded_list = sorted(sentente, reverse=True)
print(sorded_list)

sort_lengh = len(sorded_list)
print(sort_lengh)
