'''
my_list = []

name = "Tomas"
age = 15
my_list.append(name)
my_list.append(age)



print(my_list)
'''
'''
my_list = [1, 1, 2 ,3 ,4 ,5]
print(my_list)
print(my_list.count(1)) # skaiciuoja kiek yra nurodytu vienetu
my_list.append(200)
print(my_list)
my_list.insert(3,500)

print(f"Naujas listas: {my_list}")

my_list.remove(500) #panaikina tik viena pirma sutikta reiksme

print(f"Naujas listas ismetas pridetas: {my_list}")
'''
my_list = [1,2,3,4,5,6]
# print(len(my_list))
# print(min(my_list))
# print(max(my_list))
my_list2 = []
for a in my_list:
    a= a+15
    my_list2.append(a)
    
print(my_list2)   
print("loop is done")
 
