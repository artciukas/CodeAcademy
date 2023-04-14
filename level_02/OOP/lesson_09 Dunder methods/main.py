# Task Nr.1:

# Create a class called Product that takes a name and price as parameters and has __str__ and __repr__ methods defined.

# The __str__ method should return a string in the format "Product: name, Price: price"
# The __repr__ method should return a string in the format "Product('name', price)"

"""
class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}"

    def __repr__(self) -> str:
        return f'Product({self.name}, {self.price})'
    
price = Product("Kefyras", 25)
print(price)
print(repr(price))
"""

# Create a class called MyQueue that has __bool__, __repr__ and __len__ methods defined.

# The __bool__ method should return True if the queue has any items and False if it is empty.
# The __repr__ method should return a string in the format MyQueue(items) where items is the list of items in the queue.
# The __len__ method should return the number of items in the queue.

"""
from typing import List, Optional

class MyQueue:
    def __init__(self, items: List[Optional[int]]) -> None:
        self.items = items

    def __bool__(self) -> bool:
        if len(self.items) == 0:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"MyQueue({self.items})"

    def __len__(self) -> int:
        return len(self.items)
    
queue_one = MyQueue([1,2,3])
print(bool(queue_one))
print(repr(queue_one))
print(len(queue_one))

"""

# Task Nr.4:

# Create three different task with real world scenario what would include 
# all magic methods we covered today and plus 3 others from the provided list.


class Employee:
    def __init__(self, name, language ,salary) -> None:
        self.name = name
        self.language = language
        self.salary = salary

    def __str__(self) -> str:
        
        return "Class of Emloyee's"
    
    def __repr__(self) -> str:
        return f"Employee name: {self.name}, work with {self.language}."
    
    def __eq__(self, other: 'Employee') -> bool:
        if isinstance(other, Employee):
            return self.name == other.name and self.salary == other.salary
        return False
    
    def __bool__(self) -> bool:
        return bool(self.salary)
    
    def print_name(self, name: str) -> None:
        """Return text from __doc__"""
        pass

    def __lt__(self, other: 'Employee'):
        return self.salary < other.salary
    
    def __add__(self, other: 'Employee') -> int:
        if isinstance(other, Employee):
            return self.salary + other.salary
    

first_employee = Employee("Tom", "Java", 3000)
two_employee = Employee("John", "Python", 3000)
three_employee = Employee("Tim", "Python", 0)

print(first_employee)
print(repr(first_employee))
print(repr(two_employee))
print(first_employee == two_employee)
print(bool(three_employee))
print(Employee.print_name.__doc__)
print(Employee.print_name.__annotations__)
print(first_employee.salary<two_employee.salary)
v3 = first_employee + two_employee
print(v3)



