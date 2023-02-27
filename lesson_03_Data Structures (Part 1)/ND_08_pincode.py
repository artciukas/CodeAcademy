"""
1. create 4 digit pin code that is either string or int
 
2. create brute force algorithm that finds the correct pin code.
 
3. print that code
"""

pincode = 9999

i = 0

while True:
    if i != pincode:
        i = i + 1
    else:
        print(pincode)
        break