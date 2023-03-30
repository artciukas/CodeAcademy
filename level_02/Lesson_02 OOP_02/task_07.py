"""
Create a class Person that has two methods: 
set_name and set_age, which set the name and age attributes of the class, respectively. 
Modify these methods to return self, so that the calls can be chained together.
"""


class Person:
    def __init__(self) -> None:
        self.name = None
        self.age = None

    def set_name(self):
        self.name = "Tim"
        return f"Persone name is: {self}"
    
    def set_age(self):
        self.age = 25
        return f"Persone age is: {self}"
    
person_one = Person()

print(person_one.set_name())

person_one.set_age()

