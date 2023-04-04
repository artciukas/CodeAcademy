# Create a class method to return the factorial of a given number.

class Class:
    
    def __init__(self, number: int) -> None:
        self.number = number

    @classmethod
    def get_factorial(self, number: int) ->float:
        fact = 1
        for i in range(1, number+1):
            fact = fact * i
        return fact
 
number_one = Class.get_factorial(number = 12)

print(f"The factorial of {number_one} is : ", end="")
print(number_one)

