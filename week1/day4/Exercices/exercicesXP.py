# #Exercise 1
# #Instructions 
# #Create a function that displays a message about what you’re learning.
def display_message():
    print("I am learning about functions in Python")
display_message()  
# #Exercise 2
# #Instructions
# #Create a function that displays a message about a favorite book.
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")
# #Exercise 3
# #Instructions
# #Create a function that describes a city and its country.
def describe_city(city, country = "Unknown"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
# #Exercise 4
# #Instructions
# #Create a function that generates random numbers and compares them.
import random 
def function_random_number(number):
    random_number=random.randint(1, 100)
    if number==random_number:
        print("Success!")
    else:
        print(f"Fail! your number : {number} , random number {random_number}.")
function_random_number(5)
# #Exercise 5
# #Instructions
# #Create a function to describe a shirt’s size and message, with default values.
def make_shirt(size, text):
    print(f"The shirt size is {size} and it will display the message: '{text}'.")
make_shirt("S", "I love Python!")
def make_shirt(size="large", text="I love Python"):
    print(f"The shirt size is {size} and it will display the message: '{text}'.")
make_shirt()
make_shirt("medium",)
make_shirt("small", "Keep Coding and Learning!")
# #Exercise 6
# #Instructions
# #Modify a list of magician names and display them in different ways.
magician_names =['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for name in magician_names:
        print(name)
show_magicians(magician_names)
def make_great(magician_names):
    for i in range(0,len(magician_names)):
        magician_names[i] = "The Great "+ magician_names[i]
    print(magician_names)
make_great(magician_names)
# #Exercise 7
# #Instructions
# #Generate a random temperature and provide advice based on the temperature range.
def get_random_temp():
    return round(random.uniform(-10, 40), 1)
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0 :
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 < temp < 16 :
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temp < 23 :
        print("Nice weather")
    elif 23 < temp < 32 :
        print("A bit warm, stay hydrated.")
    elif 32 < temp < 40 :
        print("t’s really hot! Stay cool.")
main()
#BONUS       
month = int(input("Enter the month number (1–12): "))
def get_random_temp_B(month):
    if month in [12, 1, 2]:
        return round(random.uniform(-10, 10), 1)
    elif month in [3, 4, 5]:
        
        return round(random.uniform(10, 20), 1)
    elif month in [6, 7, 8]:
        
        return round(random.uniform(20, 40), 1)
    elif month in [9, 10, 11]:
       
        return round(random.uniform(10, 25), 1)
    else:
        print("Invalid month number! Please enter 1–12.")
        return None
def mainB():
    temp = get_random_temp_B(month)
    if temp is not None:
        print(f"The temperature right now is {temp}°C.")
        if temp < 0:
            print("Brrr, that’s freezing! Wear some extra layers today.")
        elif temp < 16:
            print("Quite chilly! Don’t forget your coat.")
        elif temp < 23:
            print("Nice weather.")
        elif temp < 32:
            print("A bit warm, stay hydrated.")
        else:
            print("It’s really hot! Stay cool.")
mainB()
