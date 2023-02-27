
# args tai yra argumentaibe kays. kvarks yrs sukejais
# ctrl+shift+p ir python linting klaidu taisymo problemo sprendimo irankis
# po argumenti eina kvargs ir pto vel negalibuti argymentu.
# mandatory gali buti ne tik vienas gali buti ir daugiau

from typing import Callable, 

def check_arguments(mandatory: Any, *args, **kwargs) -> None: # none del to nes funkcija nieko negrazina
    print(mandatory)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

# LAMBDA
# 
# WITHOUT landa

def multiply(x: int,y: int) -> int:
    return x * y

print(multiply(2,3))
# with landa

multiplication =  lambda  x,y :  x * y
print(multiplication(2,3))

# norint issikviesti funkcija funkcijosj rasoma my_function()() antri sklaiustai iskviesti tarkim lambda
# jei funkcija grazina funkcija tai ja reikia iskviesti is naujo.
# naming convensions

from typing import Callable
def my_func(n: int) -> Callable:
    return lambda a: a**: my_doubler = my_func(2)
print(my_doubler(11))