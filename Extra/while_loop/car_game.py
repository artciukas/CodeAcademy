"""help_command = "help"
start_cammand = "start"
stop_command = "stop"
quit_command = "quit"
input_command = ''

while input_command != "quit":
    input_command = input("Please enter command: ")
    if input_command == "help":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif input_command == "start":
        print('Car started...')
    elif input_command == "stop":
        print('Car is stoped')
    elif input_command == "quit":
        print('Game over, Thanks')
        break
    else:
        print("I don't understand that...")
"""

command = ""
started = False

while True :
    command = input('Please enter command:' ).lower()
    if command == "start":
        if not started:
            print("Car is already started")
        else:
            started = False
            print('Car is started')
    elif command == "stop":
        if started:
            print("Car already stoped")
        else:
            started = True
            print('Car is stoped')
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
print("Thank's for a game!!!")

