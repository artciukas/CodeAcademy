list = ['Pirmas', 'Antras', 'Trecias', 'Ketvirtas', 'Penktas']
other_list = [1, 34, 1,5, 'Tekstas']

elementu_ilgis = print(len(list))
elemento_tipas = print(type(list))
# listo_kontravimas = list(('Pirmas', 'Antras', 'Trecias'))
listo_elementas = print(list[3])
paskutinis_elementas = print(list[-1])
imtinas_elementu_emimas = print(list[1:4])
nuo_pradzios_iki_elemento = print(list[:3])
nuo_elemento_iki_pabaigos = print(list[3:])
nuo_pagaigos = print(list[-4:-1])

# Tikrinama ar yra elementas
if 'Pirmas' in list:
    print('Pirmas yra liste')

# Elemento keitimas
list[1] = ['Pakeistas']
list[1:2] = ['Keitimas1', 'Keitimas2']
list.insert(2, 'Insertuotas')
list.append('appended')
list.extend(other_list)
list.remove('Penktas')
remove_spec_index = list.pop(0) 
remove_last_element = list.pop()
del list[1]
del list
list.clear()
print(list)