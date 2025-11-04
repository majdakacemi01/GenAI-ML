# #Exercice 7
# #Instructions 
# #Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# #Store these fruits in a list.
# #Ask the user to input the name of any fruit.
# #If the fruit is in their list of favorite fruits, print:"You chose one of your favorite fruits! Enjoy!"
# #If not, print:"You chose a new fruit. I hope you enjoy it!"
favorite_fruits = input("Enter your favorite fruits (separated by spaces): ")
favorite_fruits_list = favorite_fruits.split()
chosen_fruit = input("Enter the name of a fruit: ")
if chosen_fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
# #Exercice 8
# #Instructions 
# #Write a loop that asks the user to enter pizza toppings one by one.
# #Stop the loop when the user types 'quit'.
# #For each topping entered, print:"Adding [topping] to your pizza."
# #After exiting the loop, print all the toppings and the total cost of the pizza.
# #The base price is $10, and each topping adds $2.50
topping_list=[]
while True:
    topping = input("Enter the topping of the pizza (to stop type 'quit')")
    if topping.lower() == "quit":
        break
    else:
        topping_list.append(topping)
        print(f"Adding {topping} to your pizza")
base_price = 10
topping_price = 2.5
total_cost = base_price + (len(topping_list) * topping_price)
print("Your pizza toppings:")
for t in topping_list:
    print("-", t)

print(f"Total cost: ${total_cost:.2f}")        
# #Exercice 9
# #Instructions 
# #Ask for the age of each person in a family who wants to buy a movie ticket.
# #Calculate the total cost based on the following rules:
# #Free for people under 3.
# #$10 for people aged 3 to 12.
# #$15 for anyone over 12.
# #Print the total ticket cost
price = 0
while True:
    age_input = input("What is your age (type Q to stop): ")
    if age_input.upper() == 'Q':
        break
    age = int(age_input)
    if age < 3:
        price += 0
    elif 3 <= age <= 12:
        price += 10
    else:
        price += 15
print(f"The total price is : {price}")
# #Bonus:
# #Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# #Write a program to:
# #Ask for each person’s age.
# #Remove anyone who isn’t allowed to watch.
# #Print the final list of attendees.
# Create an empty list to store ages
ages = []
while True:
    age_input = input("Enter age (or type 'done' to finish): ")
    if age_input.lower() == 'done':
        break
    age = int(age_input)
    ages.append(age)
allowed = [age for age in ages if 16 <= age <= 21]
print("Final list of attendees:")
print(allowed)