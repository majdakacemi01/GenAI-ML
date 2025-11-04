# #Exercice 1
# #Instructions 
# #Write code that concatenates two lists together without using the + sign.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
# #Exercice 2
# #Instructions 
# #Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range(1500, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
# #Exercice 3
# #Instructions
# #Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")
if user_name in names:
    print("The index of the first occurrence is:", names.index(user_name))
else:
    print("Sorry, your name is not in the list.")
# #Exercice 4
# #Instructions
# #Ask the user for 3 numbers and print the greatest number.
numbers = []
for i in range(1,4):
    number=int(input(f'Input the {i} number:'))
    numbers.append(number)
greatest = max(numbers)
print("The greatest number is:", greatest)
# #Exercice 5
# #Instructions
# #1.Create a string of all the letters in the alphabet
# #2.Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    if letter in "aeiou":
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
# #Exercice 6
# #Instructions
# #1.Ask a user for 7 words, store them in a list named words.
# #2.Ask the user for a single character, store it in a variable called letter.
# #3.Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# #4.If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter
words = []
print('I want you to enter 7 words :)')
for i in range(1,8):
    word=input(f'Enter word number {i} :')
    words.append(word)
letter=input("Enter a single letter :")
for w in words:
    if letter in w:
        index = w.index(letter)
        print(f"In the word '{w}', the letter '{letter}' first appears at index {index}.")
    else:
        print(f"The letter '{letter}' does not exist in the word '{w}'.")
# #Exercice 7
# #Instructions
# #Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
# Create a list of numbers from 1 to 1,000,000
numbers = list(range(1, 1_000_001))
print('Minimum number:', min(numbers))
print('Maximum number:', max(numbers))
total = sum(numbers)
print('Sum of all numbers:', total)
# #Exercice 8
# #Instructions
# #Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Accept comma-separated numbers from the user
numbers = input("Enter numbers separated by commas: ")
numbers_list = numbers.split(',')
numbers_tuple = tuple(numbers_list)
print("List:", numbers_list)
print("Tuple:", numbers_tuple)
# #Exercice 9
# #Instructions
# #1.Ask the user to input a number from 1 to 9 (including).
# #2.Get a random number between 1 and 9. Hint: random module.
# #3.If the user guesses the correct number print a message that says Winner.
# #4.If the user guesses the wrong number print a message that says better luck next time.
# #5.Bonus: use a loop that allows the user to keep guessing until they want to quit.
# #6.Bonus 2: on exiting the loop tally up and display total games won and lost
import random
number=input("Enter a number from 1 to 9 (type exit to stop):")
random_number = random.randint(1, 9)
wins=0
loses=0
while True:
  if number == "exit":
    break
  number= int(number)
  if number < 1 or number > 9 :
    number=int(input("please enter the number FROM 1 TO 9 :"))
  elif number == random_number:
    print('WINNER !!')
    wins+=1
  elif number != random_number:
    print("Better luck next time")
    loses+=1
print(f"Game over! You won {wins} times and lost {loses} times.")