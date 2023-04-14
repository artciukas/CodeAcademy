"""
Užduotis Nr.2:

Sukurti iš transporto priemonės klasės paveldimas klases: Autobusas, Taksi, Traukinys.
Viršklasėje įgyvendinkite bent penkis metodus, kurie apibūdintų šias transporto priemones.
Numatytasis bet kurios transporto priemonės bilieto mokestis yra sėdimų vietų skaičius * 100 . Jei Transporto priemonė yra Autobusas
egzempliorius, turime pridėti papildomus 10 % prie visos kainos kaip techninės priežiūros mokestį.

Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
Implement at least five methods in a superclass what would describe those vehicles.
The default fare charge of any vehicle is seating capacity * 100. 
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.

"""

class Vehicle:
    def __init__(self, name: str, year: int, number_of_seats: int, ticked_price: float) -> None:
        self.name = name
        self.year = year
        self.number_of_seats = number_of_seats
        self.ticked_price = ticked_price


    def get_name(self) -> str:
        return f"Vehicle name is {self.name}"
    
    def get_year(self) -> str:
        return f"{self.name} is {self.year}"
    
    def get_seats(self) -> str:
        return f"{self.name} have {self.number_of_seats} seats"
    
    def get_fare_charge(self) -> int:
        fare_charge = self.number_of_seats * 100
        return fare_charge 
    
    def ticket_profitability(self):
        ticket_profitability = self.number_of_seats * 0.50
        return ticket_profitability
    

class Bus(Vehicle):
    def __init__(self, name: str, year: int, number_of_seats: int, guide_seats: bool, ticked_price: float) -> None:
        super().__init__(name=name , year=year, number_of_seats=number_of_seats, ticked_price=ticked_price)
        self.guide_seats = guide_seats

    def get_guide_seats(self):
        return self.guide_seats
    
    def get_fare_charge(self) -> int:
        return super().get_fare_charge() * 50
    
    

class Taxi(Vehicle):
    def __init__(self, name: str, year: int, number_of_seats: int, ticked_price: float) -> None:
        super().__init__(name=name, year=year, number_of_seats=number_of_seats, ticked_price=ticked_price)
        

    

class Train(Vehicle):
    pass

bus1 = Bus("Ikarus", 2000, 55, True, 0.5)
print(bus1.guide_seats)
print(bus1.get_fare_charge())
print(bus1.ticket_profitability())
