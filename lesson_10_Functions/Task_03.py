"""
Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.
"""


user_input = input("Please enter numbers: ").split(" ")
right_sign = ["+", "-", "*", "/"]

number1, sign, number2 = user_input
int_number1 = int(number1)
int_number2 = int(number2)

def calculator(int_number1 , salyga, int_number2):
    if salyga == "+":
        answer = int_number1 + int_number2
        return answer
    elif salyga == "-":
        answer = int_number1 - int_number2
        return answer
    elif salyga == "*":
        answer = int_number1 * int_number2
        return answer
    elif salyga == "/":
        answer = int_number1 / int_number2
        return answer
    else:
        for sign in right_sign:
            if sign != right_sign:
                message = "Please enter valid sign"
                return message
        
    

print(calculator(int_number1, sign, int_number2))
print(calculator(int_number1, sign, int_number2))
print(calculator(int_number1, sign, int_number2))
print(calculator(int_number1, sign, int_number2))