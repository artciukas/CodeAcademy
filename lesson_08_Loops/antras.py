secrite_number = 9

i  = 0


while i<3:
    input_number = int(input('Please enter number: '))
    i = i + 1
    if input_number == secrite_number:
        print('You Win')
        break
else:
    print('You lose')
     


