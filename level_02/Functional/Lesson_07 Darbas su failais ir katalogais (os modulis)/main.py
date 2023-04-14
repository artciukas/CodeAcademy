# https://github.com/DonatasNoreika/python1lygis/wiki/Darbas-su-katalogais-ir-failais

import os
import sys
import pickle

# print(sys.platform) #parodo kokia operacine
# # print(dir(os))
# print(os.name)
# print(os.getcwd()) #parodo vieta is kur leidziasi skriptas

# os.chdir('/home/zbook_ubuntu/Documents')
# print(os.getcwd())
# print(os.listdir())


# os.mkdir("ne folder") 
# os.mkdir("/home/zbook_ubuntu/Documents/CodeAcademy/level_02/Lesson_07 Darbas su failais ir katalogais (os modulis)/new_folder")
# relative ir absiliut kelias


# # os.makedirs("new_folder2/something")

# w = write
# a = append
# r = read
# r+ = read and append

# encoding="utf-8 = chapteriu encodinimas(LT raides)
# https://blog.hubspot.com/website/what-is-utf-8

# nuskaito ir padaro kopija nukopijuojama visus bitus
# rb = read bite(kopijos)
# wb = write bites readina per bites.

# import pickle 
# biblioteka kur galime laikyti faile pitono objektus
# vienas picle gali priimti kelis objektus
# jie yra binary

# EOFError = end of file error


# su with automatikai fala uzdaro.
with open("/home/zbook_ubuntu/Documents/CodeAcademy/level_02/Lesson_07 Darbas su failais ir katalogais (os modulis)/failas.txt", 'r') as failas:
    failas.write("Hello world!")

# arba palieka atvira:
# failas = open("failas.txt", 'w')
# failas.write("Sveikas, pasauli!")
# failas.close()