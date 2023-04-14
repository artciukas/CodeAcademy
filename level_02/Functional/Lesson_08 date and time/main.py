# https://github.com/DonatasNoreika/python1lygis/wiki/Boolean,-data,-laikas,-i%C5%A1imtys
# bibliotekos
# datetime
# time
"""
data class work with date(sukuria datos objekta)
datatime.date(2022,1,3) - datos ivesimui
now = datetime.date.today() - parodo siandienos data
print("Year: ", now.year)
print("Month: ", now.month)
print("Day: " now.day)

####################################
time class work with time(sukuria laiko objekta)
time1 = datetime.time(10,45,24, 45567) (milisekundes iki miliono)
print("Hour: ", time1.hour)
print("Minite: ", time1.minite)
print("Second: ", time1.second)

#####################################
datatime class work with date and time

date_obj = datetime.datetime(2022,01,01,23,55,15)
print(date_obj.date()) atskiria data
print(date_obj.time()) atskiria laika
current_datetime = datetime.datetime.now() 
######################################
timedelta - skirtumas tarp dvieju datu

time_now = datetime.datetime.now()
next_newyear = datetime.datetime(2023.1.1)
time_remaining = time_now - next_newyear
print(time_remaining)

#######################################
strftime - The strftime() method returns a string representing date 
            and time using date, time or datetime object.
strftime() object -> strings

time_now = datetime.datetime.now()
string_date = time_now.srtftime(%A, %B, %d, %Y) - CIA FORMUOTI KAIP STRINGA!!!!!

#######################################
strptime - The strptime() method converts strings to datetime objects.
strings -> strptime() object

date_string = "21 June, 2021"
to_data_obj = datetime.datetime.strptime(date_string, %d %B, %Y)
print("Date object: ", date_obj)

"""
# import datetime

# x = datetime.datetime.today()
# print(x)
# print(x.)


# import datetime
# y = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(y)
# # 2020-02-29 18:20:50

# print(y.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, 'lt_LT.UTF-8')
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))

# import datetime

# pradzia = datetime.datetime.today()
# for x in range(1000000):
#     print("Labas")

# pabaiga = datetime.datetime.today()
# print(f"Programa užtruko {(pabaiga - pradzia).total_seconds()}")

# import time

# for x in range(1000000):
#     print("Labas")
#     time.sleep(2)


######################Task_02####################

# Parašyti programą, kuri:

# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)


# import datetime

# time_now = datetime.datetime.now()
# print(time_now)
# minus_five_days = time_now - datetime.timedelta(days=5)
# print(minus_five_days)
# minus_eight_hours = time_now + datetime.timedelta(hours=8)
# print(minus_eight_hours)

# time_format = time_now.strftime("%Y %m %d %H:%M:%S")
# print(time_format)

####################Task_03######################

# 1) Write a function that calculates difference in days between two datetimes. 

# import datetime

# time = datetime.datetime.now()
# birthday = datetime.datetime(1982, 12, 20)
# time_in_days = time - birthday
# print(f"You are {time_in_days.days} days old :)")


# 2) Write a function that takes a datetime object, 
# which will represent employees starting work day. 
# and will return amount of total holidays gained during the work until today. 
# 1 Month = 1.6 day off

# from datetime import datetime, date

# def get_holidays(starting_date: date) -> int:
#     return int(
#         (
#         12 * (date.today().year - starting_date.year)
#         + date.today().month
#         - starting_date.month
#         )
#         * 1.6
#     )
# starting_date = date(2022,12,1)
# print(date.today().year)
# print(date.today().month)
# print(get_holidays(starting_date))




# 3) find next 3 Fridays that happend to be Friday the 13th (classic)
# import datetime
# date = datetime.date.today()
# fridays = []
# while True:
#     if date.weekday()==4 and date.day == 13:
#         fridays.append(date)
#         date = date + datetime.timedelta(days=1)
#     date = date +datetime.timedelta(days=1)
#     if len(fridays) == 3:
#         break
# print(fridays)

# # arba

# today = datetime.datetime.now()

# i = 0

# while i < 3:
#     today = today + datetime.timedelta(days=1)
#     if today.strftime("%A %d") == "Friday 13":
#         print(today)
#         i +=1
    
# 4) Write a python function that takes nothing but returns the datetime object of last Friday



# 5) Write a Python program to get the last day of a specified year and month, 
# Example: Monday, Tuesday etc.




# 6) Write a terminal program that required user to login. 
# If user does not have an account he should register. 
# Credentials are username and password. 
# Store the information in the file txt or pickle. 
# Validate user credentials from the file. 
# Once user has logged in: print text: "Hello, <username>". 


def login():
    username_input = str(input("Please enter username: "))
   
    
    with open("database.txt", 'r') as file:
        read_from_file = file.read().split(", ")
        # print(read_from_file)
        for item in read_from_file:
            username, password = item.split(": ")
            print(username)
            if username_input == username:
                pasword_input = str(input(f"Please enter {username_input} pasword: "))
                if password == pasword_input:
                    print(f"Welcome: {username_input}")
                    break
                else:
                    print('Wrong password, tray again')
                    break
                
        if username_input != username:
            print(f"Your username: {username_input} does't exist, please register:")
            username_register = input("Please enter username: ")
            password_register = input("Please enter password: ")
            repeted_registred_password = input("Please repite pasword again:")
            if password_register == repeted_registred_password:
                with open("database.txt", 'a') as file:
                    file.write(f", {username_register}: {password_register}")
                    print("Your registration successful")
               

login()
kjahsdkjha



    







