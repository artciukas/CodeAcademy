"""
A country can be said as being big if it is:

Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

Population is greater than 20 million.
Area is larger than 3 million square km.
Also, create a method which compares a country's population density to another country object. Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}
Examples:

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"
"""

class Country:
    def __init__(self, country, population, area):
        self.country = country
        self.population = population
        self.area = area
    
    def is_big(self):
        if self.population > 20000000 and self.area > 3000000:
            status = True
        else:
            status = False
        return status
    
    def compar(self, second: "Country" ):
        if (self.population / self.area) > (second.population / second.area):
            return f'{self.country} has a lager population density than {second.country}'
        else:
            return f'{second.country} has a lager population density than {self.country}'
        




australia = Country("Australija", 23545500, 7692024)
andora = Country("Andora", 76098, 468)
print(Country.is_big(australia))
print(Country.is_big(andora))

print(andora.compar(australia))
