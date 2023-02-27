"""
Write a function that moves all elements of one type to the end of the list:

move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
Log out inputs and results in a file.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')



def move_number_to_end(number:str, array: str) -> None:
    
    try:
        int_number = int(number)
        str_to_list = list(array.split(','))
        list_item_to_int = list(map(int, str_to_list))
        
        logging.debug(f'Array entered by You: {array}')
        logging.debug(f'Your number to move at the end: {number}')
        
        for item in list_item_to_int:
            if item == int_number:
                list_item_to_int.remove(item)
                list_item_to_int.append(item)
        logging.debug(f"Finaly converted array: {list_item_to_int}")
    
    except ValueError:
        logging.debug("ERROR: Please enter numbers separate with comma")
    except Exception as err:
        logging.debug(f"Error: {err}")



if __name__ == "__main__":
    my_array = input("Please enter numbers array with koma: ")
    my_number = input("Please enter number: ")
    move_number_to_end(number = my_number, array=my_array)

# Klausimai:
# Kaip aprasyti exept jei padariai pirmame inpute klaida ir neleistu vesti antro inputo?