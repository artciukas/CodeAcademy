"""
Apibrėžkite Shape klasę su šiais atributais ir metodais:

Atributas name, kuris yra eilutė, reiškianti formos pavadinimą.
Atributas sides, kuris yra sveikasis skaičius, reiškiantis figūros kraštinių skaičių.
metodas area, kuris grąžina figūros plotą.
Tada apibrėžkite stačiakampio klasę, kuri paveldi iš formos klasės ir turi šiuos atributus bei metodus:

atributas width, kuris yra kintamasis, reiškiantis stačiakampio plotį.
Aukščio atributas, kuris yra kintamasis, žymintis stačiakampio aukštį.
Metodas init, kuris inicializuoja pavadinimą, kraštines, plotį ir aukštį.
metodas area, kuris pakeičia klasės Shape metodą area ir grąžina stačiakampio plotą.

Galiausiai apibrėžkite Square klasę, kuri paveldi iš Rectangle klasės ir turi šiuos atributus bei metodus:

Atributas side_length, kuris yra kintamasis, reiškiantis kvadrato kraštinių ilgį.
Metodas init, kuris inicializuoja atributą side_length ir iškviečia klasės Rectangle metodą init, 
kad būtų inicializuotas vardas, kraštinės, pločio ir aukščio atributus.
"""

class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def get_shape_area(self):
        return self.sides * self.sides
    
class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle", 4)
        self.width = width
        self.height = height

    def get_rectangle_area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self, side_length: int) -> None:
        super().__init__(side_length, side_length)
        self.side_length = side_length

square = Square(5)
print(square.name)
print(square.sides)
print(square.get_shape_area()) 



