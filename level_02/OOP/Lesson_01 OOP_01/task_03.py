"""
Define the Animal, Mammal, and Primate classes.
Animal should have a name attribute and a make_noise() method.
Mammal should have a warm_blooded attribute and a give_birth() method.
Primate should have an opposable_thumbs attribute and a swing() method.
Test the classes by creating a Chimpanzee and making it do various things :) monkey
"""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_noise(self):
        return print(f'{self.name} make noise!!!')

class Mummal(Animal):
    def __init__(self, name, warm_blooded: bool) -> None:
        super().__init__(name=name)
        self.warm_blooded = warm_blooded
    
    def give_birth(self):
        return print(f'Mummal {self.name} birthday!!!')

class Primate(Mummal):
    def __init__(self, name, warm_blooded: bool, opposable_thumbs) -> None:
        super().__init__(name=name, warm_blooded=warm_blooded)
        self.opposable_thumbs = opposable_thumbs
        
    def swing(self):
        return print(f"{self.name} swinging!!!")
    
primate = Primate('Chimpanzee', True, "hand")
primate.make_noise()
primate.give_birth()
primate.swing()