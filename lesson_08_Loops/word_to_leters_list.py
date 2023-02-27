word_list1 = ["pirmas", "antras", "trecias"]
word_list2 = ["ketvirtas", "penktas", "sestas"]
word_list3 = ["septintas", "astuntas", "devintas"]

output = ""
all_words = word_list1 + word_list2 + word_list3
for word in all_words:
    for leter in word:
        output = output + leter + " "



list_of_letters = output.split(" ")
print(list_of_letters)