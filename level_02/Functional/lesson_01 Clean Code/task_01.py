class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def say_hello(self) -> None:
        print(f"Hello, {self.name} {self.surname}.")


person = Person("Tim", "Smith")
person.say_hello()
