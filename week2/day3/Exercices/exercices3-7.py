# #Exercice 3
import string
import random

letters = string.ascii_letters 


random_string = ''
for i in range(5):
    random_string += random.choice(letters)

print(random_string)

# #Exercice 4
import datetime

def display_current_date():
    current_date = datetime.date.today()   
    print("Today's date is:", current_date)

display_current_date()

# #Exercice 5

def time_until_new_year():
    now = datetime.datetime.now()
    
    next_year = now.year + 1
    new_year = datetime.datetime(next_year, 1, 1)
    time_left = new_year - now
    
    print(f"Time left until January 1st {next_year}: {time_left}")

time_until_new_year()
# #Exercice 6

def minutes_lived(birthdate_str):
    birthdate = datetime.datetime.strptime(birthdate_str, "%d/%m/%Y")

    now = datetime.datetime.now()
    
    diff = now - birthdate
    
    minutes = diff.total_seconds() / 60
    
    print(f"You have lived approximately {int(minutes):,} minutes.")

minutes_lived("14/11/2000")
# #Exercice 7
from faker import Faker

users = []

def generate_users(number_users):
    fake = Faker()
    for _ in range(number_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

generate_users(3)

for user in users:
    print(user)
