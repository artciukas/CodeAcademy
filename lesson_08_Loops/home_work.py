'''
# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.
'''
import random

list_of_letters = ['a', 'b', 'c', 'd']
new_list = []
word = ""
random_range = random.randrange(5, 15)
print(random_range)
i = 0
times = 0



while i < random_range:

    leter_random = random.choice(list_of_letters)
    word = word + leter_random
    i = i + 1
    
# print(word)

new_list.append(word)
print(new_list)










