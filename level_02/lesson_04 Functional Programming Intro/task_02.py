# Sorted section:
# task_01
"""
Write a Python program to sort a list of tuples using Lambda. 
Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 
Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_list = original_list.sort(key = lambda a: a[1])

print(sorted_list)


# task_02
"""
Write a Python program to sort a list of dictionaries buy color value using Lambda.Original list of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] Sorting the List of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
# original_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 
# original_dict.sort(key=lambda x : x['color'])
# print(original_dict)


# task_03
"""
Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.Original Matrix:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]] Sort the said matrix in ascending order according to the sum of its rows
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
Original Matrix:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
"""

