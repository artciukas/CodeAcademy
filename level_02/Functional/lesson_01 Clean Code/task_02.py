full_name = "Tim Smith"


def greet(full_name: str) -> None: 
    """Function greets a person given full name as a string"""

    print(f"Hello {full_name.split()[0]} {full_name.split()[1]}, how are you today?")


greet(full_name)
