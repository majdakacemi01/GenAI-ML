#-------------------BASICS VALUES TYPES--------------------------
#STRINGS
description = "strings are..."
descriptionU = description.upper()

descriptionR = description.replace('are' , 'is')
print(descriptionU)
print(descriptionR)
print(description.split()[0])

#NUMBERS
my_age = 20 + 123879
print(my_age)

#TYPE CASTING 
bank_balance = '33000'
phone_number = 532287514

print(type(bank_balance))
print(type(phone_number))

bank_balance=int(bank_balance)
phone_number=str(phone_number)
print(type(bank_balance))
print(type(phone_number))

#Adding data types together
first_name = 'Majda'
last_name = 'Kacemi'
full_name = first_name + " " + last_name
print(full_name) 

#Booleans
x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"
print( x < y and y > z)
print(word1 == word2)
print(bool(z))
print(bool(word1))
#-------------------VARIABLES--------------------------
#EXERCICE 1
name = "Alice"
age = 30
city = "New York"
print(f"Hello, {name}! You are {age} years old and live in {city}.")
print("Hello, {}! You are {} years old and live in {}.".format(name,age,city))

#EXERCICE 2
age_2=input('Give me your age :')
years= 100 - int(age_2)
print(f"You will turn 100 in {years} years")

#-------------------CONDITIONALS--------------------------
#EXERCICE 1
name_2 = input('Entre your name')
if len(name_2) < 5:
  print('You have a short name :)')
#EXERCICE 2
num =int(input('entre a number between 1 and 100'))

if num % 3 == 0 and num % 5 == 0 : 
 print("FizzBuzz")  
elif num % 3 == 0 :
 print('Fizz')
elif num % 5 == 0 :
 print('Buzz')