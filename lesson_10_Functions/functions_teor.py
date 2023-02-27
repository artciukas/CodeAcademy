a = 2
b = 5

def  addition(number1, number2):
    sum = number1 + number2
    return sum
c = addition(a,b)

print(c)

def add_two_int_number(a: int, b: int) -> int: # int raso tik sau nes jo pitonas neinterpretuoja
    return a + b

number1 = add_two_int_number(1, 50)
print(number1)



from typing import Tuple, Optional # naudojant notacijas butina issimportuoti ta ka naudojame

def the_func(x: Union[int, float], y: Tuple[str, str], z: Optional[float] = None) -> str:
   return 'You called the_func with ' + str(x) + str(y) + str(z)

# Union reiksia sajunga galima kelis vienu metu galima
# Tuple reikia ivesti galima tik viena. 
# option gali grazinti arba negrazinti (gali paduot ar nepaduot, jei nepaduosi tai bus none)