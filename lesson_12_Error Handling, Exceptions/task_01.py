"""
Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions
"""




def devide(number:int) -> None:
    try:
        number / number
        print(f'Answer: {number}')
    except ZeroDivisionError:
        print("Can't devide from zero")

devide(0)


def number_input(first_number):
    try:
        integer_first_number = int(first_number)
        print(integer_first_number)
    except ValueError:
        print("Value error")

number_input("aa")

def second_func(number_one: str, number_two: int)-> None:
    try:
        result = number_one / number_two
        print(result)
    except TypeError:
        print("type not interger")

second_func(number_one = "0", number_two = 2)

    





