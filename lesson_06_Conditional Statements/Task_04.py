"""
Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.
"""

# first_number = int(input("Please enter first number: "))
# sign = str(input("Please enter sign: "))
# second_number = int(input("Please enter second number: "))

# if sign == "+":
#     sum = first_number + second_number
#     print(f"{first_number} {sign} {second_number} = {sum}")

# if sign == "-":
#     minus = first_number - second_number
#     print(f"{first_number} {sign} {second_number} = {minus}")

# if sign == "*":
#     multiplication = first_number * second_number
#     print(f"{first_number} {sign} {second_number} = {multiplication}")

# if sign == "/":
#     division = float(first_number / second_number)
#     print(f"{first_number} {sign} {second_number} = {division}")





guest_enter = input("Please enter first number, sign, second number: "). split(" ")

print(guest_enter)
right_sign = ["+", "-", "*", "/"]


first_number = int(guest_enter[0])
sign = guest_enter[1]
second_number = int(guest_enter[2])
print(first_number)



if sign == "+":
    sum = first_number + second_number
    print(f"{first_number} {sign} {second_number} = {sum}")

elif sign == "-":
    minus = first_number - second_number
    print(f"{first_number} {sign} {second_number} = {minus}")

elif sign == "*":
    multiplication = first_number * second_number
    print(f"{first_number} {sign} {second_number} = {multiplication}")

elif sign == "/":
    division = float(first_number / second_number)
    print(f"{first_number} {sign} {second_number} = {division}")
else:
    for sign in right_sign:
        if sign != right_sign:
            