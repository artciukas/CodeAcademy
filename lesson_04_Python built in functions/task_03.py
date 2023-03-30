"""
# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. 
# (first list containing all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.
"""
sentence_number = ["1", "2", "3", "4", "5"]
item = 1

for item in sentence_number: 
    list_nr = input('Please enter 5 words: ').split(" ")
    print(list_nr)
    list_number = "list_nr" + item
    print(list_number)
    lists_is = list_number + " : " + list_nr
    print(lists_is)
# print(first_list)
# soted_list = sorted(first_list, reverse=False)
# print(soted_list)



# second_list = input('Please enter 5 words')
# third_list = input('Please enter 5 words')
# four_list = input('Please enter 5 words')
# fifth_list = input('Please enter 5 words')