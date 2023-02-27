countries_and_capitals = {
    "Latvia" : {
        "capital" : "Riga",
        "population" : 2000000,
        }
    }

print(countries_and_capitals)
print(countries_and_capitals["Latvia"]["population"])
print(countries_and_capitals.get('Latvia').get('capital'))

print(countries_and_capitals.items())
print(list(countries_and_capitals.items()))

print(countries_and_capitals.keys())

print(countries_and_capitals.values()) #duoda ir tipa, ima visus velues
print(list(countries_and_capitals.values())) #padaro values lista ir galima su juo daryti ka tik norime
print(countries_and_capitals.keys()) #paima visus raktus
print(list(countries_and_capitals.keys())) #padaro keys lista ir galima su juo daryti ka tik norime




