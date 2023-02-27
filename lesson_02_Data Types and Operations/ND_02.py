"""
Sukurti programą, leidžiančią vartotojui įvesti visą sakinį
išspausdinti sakinį atbuline tvarka
spausdinti kas antrą sakinio raidę

"""

sentence = input("Please enter you sentence: ")

print(sentence[::-1]) # skaito is kitos puses
print(sentence[0::2]) # ima kas antra elementa