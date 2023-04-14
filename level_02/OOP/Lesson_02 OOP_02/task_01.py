"""
Task Nr.1:

Create an abstract class Animal with which takes name of animal as an input and initialize it. 
The create speak abstract method, to be overridden by subclasses. And get_name method which returns name of the animal.
Now create two subclasses of Animals: Dog and Cat which overrides the speak method, 
and provide the implementation which returns a string "Dog says Woof!" and "Cat says Meow!" respectively.
"""

from abc import ABC, abstractclassmethod

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> None:
        print(self.name)
    
    def get_speak(self) -> None:
        raise NotImplementedError

class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name = name)

    def get_speak(self) -> None:
        print("Dog says Woof!")

class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name = name)

    def get_speak(self) -> None:
        print("Cat says Meow!")
    

dog1 = Dog('Doggy')
dog1.get_name()
dog1.get_speak()

cat1 = Cat('Murmiau')
cat1.get_name()
cat1.get_speak()

