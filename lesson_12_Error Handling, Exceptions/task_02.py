"""
Create a function what would include full cycle of error handling (try/except/else/finally) with real world scenario example.
"""

def division_numbers(number_1: int, number_2:int) -> float:
    try:
        answer = number_1 / number_2
        return answer
    except ZeroDivisionError:
        print("Can not devide by 0")
        
    except Exception as err:
        print(f"Error: {err}")

    else:
        print("Devidion is sucess!!!")

    finally:
        print("Program is over")


print(division_numbers(number_1 = 2, number_2 = 0))

