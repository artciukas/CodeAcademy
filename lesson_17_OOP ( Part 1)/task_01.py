
"""
Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. Initiate class and show up some calculations.
"""

"""
"""
class Calculator:
    
    description: str = "Simple calculator"
    
    def __init__(self, number1: float, number2: float):
        self.number1: float = number1
        self.sign: str = sign
        self.number2: float = number2
    """
    @classmethod
    def get_numbers(cls):
        number1 = float(input("Enter number1: "))
        number2 = float(input("Enter number2: "))
        return cls(number1, number2)
    """
    # print(sign)

    def add(self):
        return self.number1 + self.number2
   
    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2


number1 = float(input("Please enter number1: "))
sign = str(input('Please enter sign: '))
number2 = float(input("Please enter number2: "))
object = Calculator(number1, number2)


if sign == "+":
      print(object.add())

if sign == "-":
      print(object.subtract())

if sign == "*":
      print(object.multiply())

if sign == "/":
      print(object.divide())

