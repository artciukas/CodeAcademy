"""
Create a function that takes one parameter as number - age , other as name which is default 'Anatnas', and some args and keywords.
Print first Name with age;
And then print all arguments with key arguments.
"""


def print_name_age_with_arguments(age: int, name: str = "Antanas", *args, **kwargs) -> None:
    print(f"Name are: {name}, age {age}")
    print(f"free arguments: {args if args else 'args not been improvided'}, free key arguments: {kwargs if kwargs else 'kwargs not been improvided'}")
    

print_name_age_with_arguments(25, "Tom", 12, "Argument", street = "Gedimino")

