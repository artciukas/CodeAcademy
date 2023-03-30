"""
Update previous task's solution using four pillars paradigm of OOP. (Minimum Encapsulation, Inheritance)
"""
"""
Inheritance - pagrindine klase turi paveldimuma

class Employee:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self._secrite_number = 555

    def print_name(self):
        print(f"Employer name: {self.name}")
    
    def print_surname(self):
        print(f"Employer surname: {self.surname}")

class It(Employee):
    def __init__(self, name: str, surname: str, level: str) -> None:
        super().__init__(name, surname)
        self.level = level 
    
    def pint_data(self):
        print(f"It employer level: {self.name} - {self.surname} - {self.level}")
        



object_parent = Employee('Tom', 'Smith')
object_parent.print_name()
object_parent.print_surname()
object_child = It('Donny', 'Tommy', 'beginer')
object_child.pint_data()
object_child.print_name()
"""



        

"""
Encapsulated -  viskas vienoje klaseje
"""

class Human:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def print_name(self)-> str:
        return f"Employer name: {self.name}"
    
    def print_surname(self)-> None:
        print(f"Employer surname: {self.surname}")

    def print_all_data(self)-> str:
        return f"Full data:\nName: {self.name},\nSurname: {self.surname}"

first_person = Human(name="Tim", surname="Smith")
print(first_person.print_all_data())




