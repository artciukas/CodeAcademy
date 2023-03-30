"""
Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

Form the fullname by simply joining the first and last name together, separated by a space.
Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.
"""


class Emploers:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return f"{self.name} {self.surname}"
    
    def email(self):
        return f"{self.name.lower()}.{self.surname.lower()}@company.com"
    

object = Emploers('Tomas', 'Sidlauskas')
print(object.fullname())
print(object.email())


    
