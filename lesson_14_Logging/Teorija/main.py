import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


# logging.debug('This is a debug message') #kaip printas, jei kazkas neveikia printinam ziurim.
# logging.info('This is an info message') # rinkti info kuri mums naudinga proramos atzvilgiu rinkti info kad surasti klaisdas
# logging.warning('This is a warning message') # jei kazkas atsitinka gali nutikti bet nebreak programos
# logging.error('This is an error message') # try, except jis bus except vietoje
# logging.critical('This is a critical message') # programa nebegali funkciouoti.  

# -------------------OUTPUT---------------------
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message

def add_few_number(a: int, b: int) -> int:
    logging.debug(f'Received numbers: a {a} and b:{b}')
    return a + b 

add_few_number(a=6, b=7)
