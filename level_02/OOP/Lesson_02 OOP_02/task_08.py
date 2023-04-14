

data_base_of_tabe = {'single': {"4":"free", "3":"fee", "2":"fee","1":"fre"}}
        
# data_base_of_tabe = {'single': {'4': {'name': 'Tom', 'surname': 'tom', 'time': '12'}, '3': {'name': 'Tom', 'surname': 'tom', 'time': '12'}, '2': {'name': 'Tom', 'surname': 'tom', 'time': '12'}, '1': {'name': 'Tom', 'surname': 'tom', 'time': '12'}}}     

name = "Tim"
surname = "Smith"
time = "15"

# data_base_of_tabe["single"]["1"] = {'name' : name, 'surname' : surname, 'time' : time}
# data_base_of_tabe["single"]["1"] = {'name': name, 'surname': surname, 'time' : time}
# print(data_base_of_tabe["single"]["1"])
# print(data_base_of_tabe["single"])

for single_table, reservation in data_base_of_tabe["single"].items():
    # print(f'{single_table} ":" {reservation}')
    if reservation != 'free':
        print("Sorry reservation is not posible")
        continue
    else:
        data_base_of_tabe["single"][single_table] = {'name': 'Tom', 'surname': 'tom', 'time' : '12'}
        break
       
        
print(data_base_of_tabe)


