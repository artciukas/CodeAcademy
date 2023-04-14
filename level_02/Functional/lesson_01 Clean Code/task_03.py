def greet_user(age: int) -> None:
    eligible_to_enter = age > 21

    if eligible_to_enter == True:
        print("Welcome")

    if eligible_to_enter == False:
        print("Access denied")


greet_user(22)
