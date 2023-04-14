"""
Create a class to represent a library system. 
The library system should have a collection of books that can be borrowed by users. 
Users can register to the library system, borrow books, and return books. 
The library system should keep track of the books borrowed by users, and the number of available copies of each book.
"""

# class Car:
#     total_cars_sold: int = 0    
#     def __init__(self, make: str, model: str):
#         self.make = make        
#         self.model = model        
#         Car.total_cars_sold += 1    
    
#     @classmethod    
#     def get_total_cars_sold(cls) -> int:
#         return cls.total_cars_sold

# car1: Car = Car('Toyota', 'Camry')
# car2: Car = Car('Honda', 'Civic')
# print(Car.get_total_cars_sold())  # 2

# class Library:
#     number = 0
#     list_01 = []
#     def __init__(self, number_tt) -> None:
#         self.number_tt =number_tt
#         self.list_02 = []
#         Library.number += 1
    
#     def get_number_list(self):
#         self.list_02.append(self.number_tt)
#         return self.list_02

#     @classmethod
#     def get_number(cls):
#         Library.list_01.append(Library.number)
#         return Library.number
    
# one = Library(1)
# two = Library(2)
# one = Library(3)
# two = Library(4)
# one = Library(1)
# two = Library(2)
# one = Library(3)
# two = Library(4)

# print(Library.get_number())
# print(Library.list_01)
# print(one.get_number_list())

class Student:
    # Class attribute
    location: str = "Parametras"
    # Class Constructor 
    def __init__(self, name, groupe) -> None:
        self.name = name
        self.groupe = groupe

    # Instance method
    def get_name(self) -> str:
        return f"The student name is: {self.name}"

    # Another instance method
    def get_groupe(self) -> str:
        return f"The student groupe are: {self.groupe}"
    
    def change_location(self):
        self.location = "Change"
        return self.location
    
first_student = Student('Petras', 'HTMT-5')
first_student.change_location().upper()
student_name = first_student.get_name().upper()
student_groupe = first_student.get_groupe().upper()
print(f"{student_name}, {student_groupe}")


call_classatribute = Student.location.upper()
print(call_classatribute)

        



