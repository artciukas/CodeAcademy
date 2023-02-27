"""
If deviseble by 3 need to return Fizz
If deviseble by 5 nedd to return Buzz
If deviseble by 5 and 3 (15) return FizzBuzz
If nondevisible by 5 and 3 return it self
"""

def fizz_buzz(input_number):
    if input_number % 3 == 0 and input_number % 5 == 0:
        return "FizzBuzz"
    if input_number % 3 == 0:
        return "Fizz"
    if input_number % 5 == 0:
        return "Buzz"
    else:
        return input_number



