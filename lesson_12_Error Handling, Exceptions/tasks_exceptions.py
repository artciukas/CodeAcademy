
# index error
"""
def list_index(number:int)->int:
    my_list = [1, 2, 3]
    try:
        return my_list[number]
    except IndexError:
        return "Index value in my list is not exist"

print(list_index(number = int(input("Enter index number:"))))

# value error

def born_age(age: int)->str:
    try:
        my_age = 2023 - age
        return f"My born age is: {my_age}"
    except ValueError:
        return "!!!Please enter only numbers!!!"
        

print(born_age(age=int(input('Please enter your age: '))))

# key error

def print_value_by_key(key: str)->str:
    try:
        my_dictionary = {"name" : "Tomas", "phone": "12236654987"}
        ditionary_value = my_dictionary[key]
        return ditionary_value
    except KeyError as ex:
        print(ex)
        print(type(ex))
        return f'Can not find {key} key on my dictionary, but we add: {my_dictionary}'
        # return f'Can not find {key} key on my dictionary'


print(print_value_by_key(key = input('Please enter key value: ')))


# devide by zero and type errors

def number_division_by(number):
    try:
        answer = 100 / number
        return f"Answer is: {answer}"
    except (ZeroDivisionError, TypeError) as e:
        return f"Error mesage is: {e.args}"

print(number_division_by(number=input("Please enter number to devide 100: ")))
    
"""
#raise exeptions

def get_value_by_key(key: str)->str:
    
    my_dictionary = {"name" : "Tomas", "phone": "12236654987", "surname": "Smith"}
    if key in my_dictionary:
        return my_dictionary[key]
    else:    
        raise KeyError(f'Can not find {key} key on my dictionary, but we add: {my_dictionary}') 
    
try: 
    surname = get_value_by_key("surname")
except KeyError:
    surname = "AAAA"

print(surname)




    



