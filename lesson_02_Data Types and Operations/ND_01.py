'''
Sukurkite programą, leidžiančią vartotojui įvesti savo vardą ir amžių
Apskaičiuoti metus, kuriais vartotojas gimė
Išspausdinti atsakymą į terminalą

'''

name = input('Enter your name: ')
age = input("Enter your age: ")
born_age = f"{name} your born age is: {2023 - int(age)}"

print(born_age)

#arba

