"""
3x3 matrix

[
    1 2 3
    4 5 6
    7 8 9
]
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] #(2)pasiima pirmos matricos antra skaiciu
matrix[0][1] = 20 # keiciama reiksme is 2 i 20

for row in matrix:
    for item in row:
        print(item)