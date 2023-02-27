"""
Create a simple program that would log all inputs from the terminal. 
Configs must show all additional data (time, date, level etc.)
"""

import logging


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')



try:
    first_input = int(input("Please enter first nummber: "))
    logging.debug(f'Entered number {first_input} is sucess')
except Exception as e:
    logging.debug(f'Error: {e}')



def devide(number: str) -> None:
    try:
        input_number = int(number)
        logging.debug(f"Entered number are: {number}")
        input_number / input_number 
        logging.debug(f'Answer number / number is: {number}')
    except ZeroDivisionError:
        logging.debug("Can't devide from zero")
    except ValueError:
        logging.debug("Please enter only numbers")


# devide(number = 0)

def print_value_by_key(key: str)->str:
    try:
        my_dictionary = {"name" : "Tomas", "phone": "12236654987"}
        ditionary_value = my_dictionary[key]
        logging.debug(f"Entered key are: {key}")
        return ditionary_value
    except KeyError as ex:
        return f'Can not find {key} key on my dictionary.'
        




if __name__ == "__main__":
    enter_number = input("Please enter number to devide it self: ")
    devide(number = enter_number)
    dict_key = input('Please enter key value: ')
    print_value_by_key(key = dict_key)

        


