# #Exercise 1
# #Instructions 
# #Print the following output using one line of code:
# #Hello world
# #Hello world
# #Hello world
# #Hello world
print(("hello world\n")*4)
# #Exercise 2
# #Instructions 
# #Write code that calculates the result of:
# #(99^3)*8 (meaning 99 to the power of 3, times 8).
print((99*99*99)*8)
# #Exercise 3
# #Instructions 
# #Predict the output of the following code snippets:
# #Coment what is your guess, then run the code and compare
#my guess will be inside the brackets infront of each code
# #>>> 5 < 3 (False)
# #>>> 3 == 3 (True)
# #>>> 3 == "3" (False)
# #>>> "3" > 3 (False)
# #>>> "Hello" == "hello" (False)
print(bool(5 < 3))
print(bool(3 == 3))
print(bool(3 == "3"))
#print(bool("3" > 3))
print(bool("Hello" == "hello"))
# #Exercise 4
# #Instructions
# #Create a variable called computer_brand which value is the brand name of your computer.
# #Using the computer_brand variable, print a sentence that states the following:
# #"I have a <computer_brand> computer."
computer_brand = "hp"
print(f"I have a {computer_brand} computer.")
# #Exercise 5
# #Instructions
# #Create a variable called name, and set it’s value to your name.
# #Create a variable called age, and set it’s value to your age.
# #Create a variable called shoe_size, and set it’s value to your shoe size.
# #Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# #Have your code print the info message.
# #Run your code.
name="Majda"
age="20"
shoe_size="39"
info=f"My name is {name}, i have {age} years old, and i wear in my shoes {shoe_size}. "
print(info)
# #Exercise 6
# #Instructions
# #Create two variables, a and b.
# #Each variable’s value should be a number.
# #If a is bigger than b, have your code print "Hello World".
a = 5
b = 2
if a > b :
 print('Hello World')
# #Exercise 7
# #Instructions
# #Write code that asks the user for a number and determines whether this number is odd or even
x = int(input("Enter a number :"))
if x % 2 == 0 :
 print('this number is an even')
else :
 print('this number is an odd')
# #Exercise 8
# #Instructions
# #Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
user_name = input('What is your name ?')
user_name=user_name.capitalize()
if name == user_name :
 print('Oh woow we have the same name!')
else :
 print(f'nice to meet you {user_name}')
# #Exercise 9
# #Instructions
# #Write code that will ask the user for their height in centimeters.
# #If they are over 145 cm, print a message that states they are tall enough to ride.
# #If they are not tall enough, print a message that says they need to grow some more to ride.
height=int(input('What is your height in centimeters?'))
if height < 145 :
 print('You need to grow some more to ride !')
else :
 print('You are tall enough to ride !')
