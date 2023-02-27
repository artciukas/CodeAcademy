from typing import Union

def divider(number: Union[float, int]) -> Union[float, int]:
    return number / 2 if isinstance(number, float) else number // 2

try:
    my_divided_number = divider(4)
    print(my_divided_number)
    print(my_divided_number / 0)

except TypeError:
    print('We are f*cked up!')

except Exception as e:
    print(f'Error: {e}')
else: #jei yra return else jau nebereikia
    print("Success")
finally: #bus ivykdomas bet kada
    print("Program is done")