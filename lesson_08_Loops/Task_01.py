"""
Create a variables containing strings for username and password. Start Endless loop allowing to enter username and password. 
If credentials are correct stop endless loop and print greeting message.

"""
# First 
"""
name = "Tomas"
password = "1234"


while True:
    input_name = input("please enter Name: ")
    input_password = input("Please enter Password: ")
    if input_name == name and input_password == password:
        print("Welcome")
        break
    print("Tray again")
    
"""

# Scond

name_and_password = ["Tomas", "1234"]

while True:
    input_name, input_password = input("Please enter Name and password: ").split()
    if name_and_password[0] == input_name and name_and_password[1] == input_password:
        print(f"Welcome {input_name}")
        break
    print("Tray again")



