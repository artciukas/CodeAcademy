"""
Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"
"""

user_name = input("Please enter your name: ")
database_list = ['Tom', 'Den', 'Trump']

if user_name in database_list:
    print(f"{user_name} greeting!!!")
else:
    print("Welcome otherwise")