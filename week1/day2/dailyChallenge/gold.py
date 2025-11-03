# #chanllenge 1
# #Instructions
# #Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
Display a little cake 
# #The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# #Bonus : If they were born on a leap year, display two cakes !
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
day, month, year = map(int, birthdate.split("/"))
from datetime import datetime

current_year = datetime.now().year
age = current_year - year
candles = age % 10
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True
else:
    leap = False
cake = "   ___" + "i"*candles + "___\n" \
       "  |:H:a:p:p:y:|\n" \
       " __|___________|__\n" \
       "|^^^^^^^^^^^^^^^^^|\n" \
       "|:B:i:r:t:h:d:a:y:|\n" \
       "|                 |\n" \
       "~~~~~~~~~~~~~~~~~~~"
if leap:
    print("It's a leap year! Here are two cakes:\n")
    print(cake)
    print()
    print(cake)
else:
    print(cake)

