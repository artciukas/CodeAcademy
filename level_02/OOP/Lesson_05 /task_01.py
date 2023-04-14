"""
Create a class which takes temperature measurements in Kelvins and 
add static methods to transform those to Celsius and Fahrenheit units. Use OOP abstraction.
"""

from abc import ABC, abstractmethod

class ConversionTool(ABC):
    
    @abstractmethod
    def to_celsius(self, number: float) -> float:
        pass

    @abstractmethod
    def to_fahrenheit(self, number: float) -> float:
        pass

class Temperature:

    @staticmethod
    def to_celsius(number: float)-> float:
        celsius = number - 273.15
        return f"Kelvin {number} is equel: {celsius} C"
    
    @staticmethod
    def to_fahrenheit(number: float)->float:
        fahrenheit = round((number - 273.15) * 9 / 5 + 32, 2)
        return f"Kelvin {number} is equel: {fahrenheit} F"

print(Temperature.to_celsius(10))
print(Temperature.to_fahrenheit(10))