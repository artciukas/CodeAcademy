

# def greeting(name: str)->str:
#     try:
#         greet = ''
#         greet = 'Hello' + name
#         return greet
#     except TypeError:
#         print('Please enter strings')
#     # else Exception as e:
#     #     print(f'Error: {e}')
    

        

# greeting(name = "Tomas")
# print(greet)



def greeting(name: str)->str:
    greet = 'Hello' + name
    return greet
    
        

message = greeting(name = "Tomas")
print(message)
