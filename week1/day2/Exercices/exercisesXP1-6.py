# #Exercice 1
# #Instructions 
# #Create a set called my_fav_numbers and populate it with your favorite numbers
my_fav_numbers = {2, 3, 5, 7}
# #Add two new numbers to the set.
my_fav_numbers.add(4)
my_fav_numbers.add(9)
# #Remove the last number you added to the set.
my_fav_numbers.remove(9)
# #Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers = {2, 3, 4, 7, 9}
# #Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
# #Exercice 2
# #Instructions
# #Given a tuple of integers, try to add more integers to the tuple.
my_tuple = (1, 2, 3)
# We cannot add more integers directly because tuples are immutable
# But we can create a new tuple by concatenation
my_tuple = my_tuple + (4, 5)
print(my_tuple)
# #Exercice 3
# #Instructions
# #You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# #Remove "Banana" from the list.
# #Remove "Blueberries" from the list.
# #Add "Kiwi" to the end of the list.
# #Add "Apples" to the beginning of the list.
# #Count how many times "Apples" appear in the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Apples")
basket.append("Kiwi")
print(basket)
n=0
for i in range(0, 4) :
    if basket[i] == "Apples":
        n+=1
print(f"Apples appear in the list {n} times")
# #Empty the list.
# #Print the final state of the list.
basket.clear()
print(basket)
# #Exercice 4
# #Instructions 
# #Recap: What is a float? What’s the difference between a float and an integer?
#A float is a number with a decimal point.
#An integer is a whole number without decimals.
# #Create a list containing the following sequence of mixed types: floats and integers:
# #1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# #Avoid hard-coding each number manually.
# #Think: Can you generate this sequence using a loop or another method?
numbers = [x * 0.5 for x in range(3, 11)]
print(numbers) 
# #Exercice 5
# #Instructions
# #Write a for loop to print all numbers from 1 to 20, inclusive.
for y in range(1,21):
    print(y)
# #Write another for loop that prints every number from 1 to 20 where the index is even.
for y in range(1,21):
    if y % 2 == 0 :
        print(y)
# #Exercice 6
# #Instructions 
# #Use an input to ask the user to enter their name.
# #Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# #hint: check for the method isdigit()
# #if the input is incorrect, keep asking for the correct input until it is correct
# #if the input is correct print “thank you” and break the loop
name = input("Enter your name please :")
while True :
    if len(name) < 3 or name.isdigit() :
        name = input("give the correct name: ")
    else :
        print("Thank you")   
        break 
