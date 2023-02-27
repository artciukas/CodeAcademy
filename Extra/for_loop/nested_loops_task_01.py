"""
Create:
xxxxx
xx
xxxxx
xx
xx
"""

numbers = [5, 2, 5, 2, 2]


for count_x in numbers:
    output = ""
    for count in range(count_x):
        output =  output + "L"       
    print(output) 

