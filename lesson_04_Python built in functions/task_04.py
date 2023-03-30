"""
print all the items separated with "|"
"""

float_list = [3.45655, 6.486666, 3.456659, 53.366654]
new_float_list = []
for item in float_list:
    item_two = round(item, 2)
    new_float_list.append(item_two)

print(new_float_list)
