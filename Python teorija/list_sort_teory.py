listas = ['Pirmas', 'Antras', 'Trecias', 'Ketvirtas', 'Penktas']


listas.sort()
print(listas)
# sortinimas yra casesensitive pirmiausia didziodiomis zodziai poto mazosiomis
listas.sort(reverse=True)
print(listas)
listas.reverse()
print(f'Rvesinis listas: {listas}')

copy_list = listas.copy()
print(f'Nukopijuotas listas: {copy_list}')

# arba

copy_list = list(listas)
print(f'Kitu budu nukopijuotas listas: {copy_list}')

