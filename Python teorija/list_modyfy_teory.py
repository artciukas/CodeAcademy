list = ['Pirmas', 'Antras', 'Trecias', 'Ketvirtas', 'Penktas']

new_list = []
new_list2 = []


for x in list:
    if 'a' in x:
        new_list.append(x)
print(new_list)

# arba List Comprehension metodas

new_list2 = [x for x in list if 'a' in x]
print(new_list2)

# sintax
# newlist = [expression for item in iterable if condition == True]
# newlist = ['hello' for x in fruits]
# newlist = [x if x != "banana" else "orange" for x in fruits]
