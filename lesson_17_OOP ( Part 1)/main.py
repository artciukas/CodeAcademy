# OOP
"""

"""



class Person:

    description: str = "A simple normal human being"

    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname
    
        
    def greet(self):
        return f"Hello, my name is {self.name} {self.surname}"
    
    
        






person = Person('Arturas','Ardzijauskas')
person2 = Person('Antanas', 'Popovas')

print(person.greet())
print(person.greet())



