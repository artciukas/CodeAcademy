numbers = [10, 1, 15, 20, 100]

numbers.append(20)
print(numbers)

numbers.insert(0, 15) # pirmas skaicius indeksas antras insertuojamas skaicius
print(numbers)

numbers.remove(15) #remove 15
print(numbers)

numbers.clear() #remove all atems
print(numbers)

numbers = [10, 1, 15, 20, 100]

numbers.pop() #remove last item in tje list
print(numbers)

numbers = [10, 1, 15, 20, 100]

print(numbers.index(1)) #return index of number

print(50 in numbers) # parodo ar yra skaicius liste


numbers = [10, 1, 10, 20, 100]
print(numbers.count(10)) #skaiciuoja kiek yra besikartojanciu desimtu liste

numbers = [10, 1, 15, 20, 100]
numbers.sort() # ima nuo maziausio iki didziausio
numbers.reverse() # ima nuo didziausio iki maziausio
print(numbers)

numbers2 = numbers.copy() # padaro listo kopija



