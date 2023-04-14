import this
from datetime import datetime

with open("file.txt", 'w') as file:
    file.write(this.s)


with open('file.txt', 'r') as file:
    print(file.read())

# with open('file.txt', 'a') as file:
#     file.write(str(datetime.today()))

with open('file.txt', 'a') as failas:
    failas.write(str(datetime.today()))