'''
# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. 
# (first list containing all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.
'''

first_list = ['Pirmas', 'Antras', 'Trecias', 'Ketvirtas', 'Penktas' ]
two_list = ['Sestas', 'Septintas', 'Astuntas', 'Devintas', 'Desimtas']
third_list = ['Pirmas', 'Antras', 'Trecias', 'Ketvirtas', 'Penktas' ]
fouhr_list = ['Sestas', 'Septintas', 'Astuntas', 'Devintas', 'Desimtas']
five_list = ['Pirmas', 'Antras', 'Trecias', 'Ketvirtas', 'Penktas' ]

first_list_new = []
two_list_new = []
third_list_new = []
fouhr_list_new = []
five_list_new = []


first_list.sort(reverse=False)
# print(first_list)
two_list.sort(reverse=False)
third_list.sort(reverse=False)
fouhr_list.sort(reverse=False)
five_list.sort(reverse=False)

first_list_new.append(first_list.pop(0))
first_list_new.append(two_list.pop(0))
first_list_new.append(third_list.pop(0))
first_list_new.append(fouhr_list.pop(0))
first_list_new.append(five_list.pop(0))
print(first_list_new)

two_list_new.append(first_list.pop(1))
two_list_new.append(two_list.pop(1))
two_list_new.append(third_list.pop(1))
two_list_new.append(fouhr_list.pop(1))
two_list_new.append(five_list.pop(1))

print(two_list_new)
third_list_new.append(first_list.pop(2))
third_list_new.append(two_list.pop(2))
third_list_new.append(third_list.pop(2))
third_list_new.append(fouhr_list.pop(2))
third_list_new.append(five_list.pop(2))
print(third_list_new)

fouhr_list.append(first_list.pop(3))
fouhr_list.append(two_list.pop(3))
fouhr_list.append(third_list.pop(3))
fouhr_list.append(fouhr_list.pop(3))
fouhr_list.append(five_list.pop(3))
print(fouhr_list_new)

.append(first_list.pop(3))
fouhr_list.append(two_list.pop(3))
fouhr_list.append(third_list.pop(3))
fouhr_list.append(fouhr_list.pop(3))
fouhr_list.append(five_list.pop(3))
print(five_list_new)





