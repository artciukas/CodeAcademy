"""
Tarkime, turime klases: A, B ir C:

Pakeiskite programą taip, kad į A klasę būtų pridėtas metodas say_hello, kuris spausdina "Sveiki iš A klasės".
Modifikuokite programą taip, kad į B klasę būtų pridėtas metodas say_hello, kuris spausdina "Hello from class B".
Modifikuokite programą, kad į C klasę būtų įtrauktas metodas say_hello, kuris spausdina "Sveiki iš C klasės".
Sukurkite C klasės objektą ir iškvieskite jam metodą say_hello. Koks bus išvesties rezultatas?
Pakeiskite programą taip, kad B klasės metodas say_hello iškviestų A klasės metodą say_hello naudodamas super() funkciją.
Sukurkite C klasės objektą ir vėl iššaukite jo metodą say_hello. Koks dabar bus išvesties rezultatas?



Lets say we have classes: A, B and C:

Modify the program to add a method say_hello to class A that prints "Hello from class A".
Modify the program to add a method say_hello to class B that prints "Hello from class B".
Modify the program to add a method say_hello to class C that prints "Hello from class C".
Create an object of class C and call the say_hello method on it. What is the output?
Modify the program so that class B's say_hello method calls the say_hello method of class A using the super() function.
Create an object of class C and call the say_hello method on it again. What is the output now?
"""

class A:
    def say_hello(self):
        print("Hello from class A")

class B(A):
     def say_hello(self):
        print("Hello from class B")
        super().say_hello()
    

class C(B):
     def say_hello(self):
        print("Hello from class C")
        super().say_hello()

c = C()
c.say_hello()
