#Functions to test user input via Postman
from datetime import datetime

#Allow user to input their name 
def get_users_name():
    users_name = input("What is your name? ")
    return users_name

#Get the current date and return 3 variables for full date, current time and current date.
def get_current_time():
    current_full_date = datetime.now()
    current_hour = str(current_full_date.hour) 
    if current_full_date.minute < 10:
        current_minute = "0"+ str(current_full_date.minute)
    else:
        current_minute = str(current_full_date.minute)
    current_time = (current_hour + ":" + current_minute)
    current_date = current_full_date.date()
    return current_full_date,current_time, current_date

#Greet the user using their name and tell them the current date and time
def greet_users(users_name,current_time,current_date):
    print(f"Hello {users_name}, welcome to ours app. The current time is {current_time} and the date is {current_date}")

