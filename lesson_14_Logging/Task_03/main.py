"""
Create 3 functions, that are related to each other (one is being called in another), and test all logger severity levels by your own design.

Function examples:

def check_engine() -> None:
  pass
 
def start_car() -> None:
  check_engine()...
.......
"""

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def data_collection(user_input:str) -> None:
    logging.debug('Im in datacollection')
    data_converter()
    return
    
def data_converter() -> None:
    
    logging.debug('Im in data converter')
    try:
        convert_to_int = int(user_input)
        logging.debug(f"Converted to int: {user_input}")
    except Exception as err:
        logging.debug("Error")

def 
        


if __name__ == "__main__":
    user_input = input("Please enter something: ")
    data_collection(user_input)
    

