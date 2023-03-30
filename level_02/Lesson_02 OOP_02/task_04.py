"""
Create a Calculator program : it should contain abstract class with methods (abstract and not), 
base class, geometry, arithmetic calculator classes. 
Every subclass should have at least 5 methods to make some meaningful calculus operations.


Sukurkite skaičiuotuvo programą: joje turėtų būti abstrakti klasė su metodais 
(abstrakčiais ir neabstrakčiais), bazinė klasė, geometrijos, aritmetinis skaičiuotuvas klases. 
Kiekviena poklasė turėtų turėti bent 5 metodus, kad būtų galima atlikti keletą prasmingų skaičiavimo operacijų.

"""

from abc import ABC, abstractmethod

class Abstract(ABC):
    def __init__(self, number_one: float, number_two: float, cube_side: float) -> None:
        self.number_one = number_one
        self.number_two = number_two
        self.cube_side = cube_side

    
    @abstractmethod
    def get_sum_of_number(self):
        pass
    
    @abstractmethod
    def get_div_of_number(self):
        pass

    @abstractmethod
    def get_cube_area(self):
        pass

class Base(Abstract):
    def __init__(self, number_one: float, number_two: float, cube_side: float) -> None:
        super().__init__(number_one, number_two, cube_side)

    def get_sum_of_number(self):
        answer = self.number_one + self.number_two
        return f"{answer}"
    
    def get_div_of_number(self):
        answer = self.number_one - self.number_two
        return f"{answer}"

    def get_cube_area(self):
        cube_area = self.cube_side * self.cube_side
        return f"Cube area: {cube_area}"
    
class Geometry(Base):
    def __init__(self, number_one: float, number_two: float, cube_side: float) -> None:
        super().__init__(number_one, number_two, cube_side)
    

class Aritmetic(Base):
    def __init__(self, number_one: float, number_two: float) -> None:
        super().__init__(number_one, number_two)

        super().get_sum_of_number
        super().get_div_of_number


aritmetic = Aritmetic(2.5, 2.5)
print(aritmetic.get_div_of_number())
print(aritmetic.get_sum_of_number())

# 0.0
# 5.0