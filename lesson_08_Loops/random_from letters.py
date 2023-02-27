'''
# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.
'''
import random

list_of_letters = ['a', 'b', 'c', 'd']
new_list = []
my_database = {}
sum_word_a_leters_are = 0
sum_word_b_leters_are = 0
sum_word_c_leters_are = 0
sum_word_d_leters_are = 0

# function generate random word
def word_printer():
    word_letters_range = random.randrange(5, 15)
    times = 0
    word = ""
   
    # word generator
    while times != word_letters_range:
        
        leter_random = random.choice(list_of_letters)
        # print(leter_random)
        word = word + leter_random
        times = times + 1
    # the number of times the function is called, we will add the number of words to the list  
    new_list.append(word)

# how many words are in list 
for x in range(5):
    word_printer()

# counting letters
for words in new_list:
    word_a_leters_are = words.count("a")
    word_b_leters_are = words.count("b")
    word_c_leters_are = words.count("c")
    word_d_leters_are = words.count("d")
    
    sum_word_a_leters_are = sum_word_a_leters_are + word_a_leters_are
    sum_word_b_leters_are = sum_word_b_leters_are + word_b_leters_are
    sum_word_c_leters_are = sum_word_c_leters_are + word_c_leters_are
    sum_word_d_leters_are = sum_word_d_leters_are + word_d_leters_are

# adding to dictionary
my_database["a leters are"] = sum_word_a_leters_are
my_database["b leters are"] = sum_word_b_leters_are
my_database["c leters are"] = sum_word_c_leters_are
my_database["d leters are"] = sum_word_d_leters_are


# printing
print(f"""
Generated list are: {new_list}
a leter are: {my_database.get("a leters are")}
b leter are: {my_database.get("b leters are")}
c leter are: {my_database.get("c leters are")}
d leter are: {my_database.get("d leters are")}
""")




