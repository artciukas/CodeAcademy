
"""
Sukurti programą, kuri:

Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, 
nuo kada dirba (data būtų nustatoma automatiškai, pagal dabartinę datą).
Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

"""

from main_task import engine, Darbuotojas
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

while True:
    pasirinkimas = int(input("Pasirinkite veiksmą: \n1 - atvaizduoti darbuotojus \n2 - irasyti darbuotoja \n3 - pakeisti darbuotoja \n4 - ištrinti darbuotoja\n0 - iseiti is programos\n"))

    if pasirinkimas == 1:
        projektai = session.query(Darbuotojas).all()
        print("-------------------")
        for darbuotojas in projektai:
            print(darbuotojas)
        print("-------------------")

    if pasirinkimas == 2:
        name = input("Įveskite darbuotojo varda: ")
        surname = input("Įveskite darbuotojo pavarde: ")
        birth_date = input("Įveskite darbuotojo gimimo metus: ")
        position = input("Įveskite darbuotojo pareigas: ")
        salary = input("Įveskite darbuotojo atlyginima: ")
        darbuotojas = Darbuotojas(name, surname, birth_date, position, salary)
        session.add(darbuotojas)
        session.commit()

    if pasirinkimas == 3:
        projektai = session.query(Darbuotojas).all()
        print("-------------------")
        for darbuotojas in projektai:
            print(darbuotojas)
        print("-------------------")
        keiciamo_id = int(input("Pasirinkite norimo pakeisti darbuotojo ID: "))
        keiciamas_projektas = session.query(Darbuotojas).get(keiciamo_id)
        pakeitimas = int(input("Ką norite pakeisti: 1 - varda, 2 - pavarde, 3 - pareigas, 4 - alga"))
        if pakeitimas == 1:
            keiciamas_projektas.name = input("Įveskite darbuotojo varda: ")
        if pakeitimas == 2:
            keiciamas_projektas.surname = input("Įveskite darbuotojo pavarde: ")
        if pakeitimas == 3:
            keiciamas_projektas.position = input("Įveskite datbuotojo pareigas: ")
        if pakeitimas == 4:
            keiciamas_projektas.surname = float(input("Įveskite darbuotojo alga: "))
        session.commit()

    if pasirinkimas == 4:
        projektai = session.query(Darbuotojas).all()
        print("-------------------")
        for darbuotojas in projektai:
            print(darbuotojas)
        print("-------------------")
        keiciamo_id = int(input("Pasirinkite norimo ištrinti darbuotojo ID: "))
        trinamas_projektas = session.query(Darbuotojas).get(keiciamo_id)
        session.delete(trinamas_projektas)
        session.commit()

    if pasirinkimas == 0:
        print('Baigeme darba!!!')
        break