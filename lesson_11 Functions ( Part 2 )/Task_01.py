"""
Write a function that takes two lists and adds the first element in the first list with the first element in the second list, 
the second element in the first list with the second element in the second list, etc, etc. 
Return True if all element combinations add up to the same number. Otherwise, return False. Example:

puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# Both lists sum to [5, 5, 5, 5]
puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
puzzle_pieces([1, 2], [-1, -1]) ➞ False
puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False
"""

first_list = [1, 2, 3, 4]
second_list = [4, 3, 2, 1]
# sum_list = []

def two_list_sum(first_list, second_list):
    
    if len(first_list) == len(second_list):
        first_dic = {}
        second_dic = {}

        for first_list_index, first_list_value in enumerate(first_list):
            first_dic = {first_list_index: first_list_value}
            print(first_dic)
        for second_list_index, second_list_value in enumerate(second_list):
            second_dic = {second_list_index: second_list_value}
            print(second_dic)
        if first_dic.keys() == second_dic.keys():
            a = first_dic.values() + second_dic.values()
            print(a)
            
            print("Lygu")
    
    else:
        # print("1")
        return False

print(two_list_sum(first_list, second_list))

