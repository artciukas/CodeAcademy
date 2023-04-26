# https://github.com/DonatasNoreika/python1lygis/wiki/Duomen%C5%B3-baz%C4%97s-2

import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///darbuotojai.db')
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = 'Darbuotojai'
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    birth_date = Column("Date of birth", String)
    position = Column("Position", String)
    salary = Column("Salary", Float)
    working_since = Column("Pradejo dirbti", DateTime, default=datetime.datetime.utcnow)
    


    def __init__(self, name, surname, birth_date, position, salary):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.position = position
        self.salary = salary


    def __repr__(self):
        return f"{self.id} {self.name}, {self.surname}, {self.birth_date}, {self.position}, {self.salary} {self.working_since}"

Base.metadata.create_all(engine)