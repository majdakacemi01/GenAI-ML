# #Exercice 1
# #Instructions
# #The point of the exercise is to check if a person can retire depending on their age and their gender
age = 0
def  get_age(year, month, day):
    
    if month < 11 :
        age = 2025 - year
    else:
        age = 2025 - year - 1
    return age

def can_retire(gender, date_of_birth) :
    year, month, day = map(int, date_of_birth.split("/"))
    age = get_age(year, month, day)
    if gender.lower() == "m" and age >= 67:
        return True
    elif gender.lower() == "f" and age >= 62:
        return True
    else:
        return False
gender = input("Enter your gender (m/f): ")
date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ")

if can_retire(gender, date_of_birth):
    print("You can retire!")
else:
    print("You cannot retire yet.")
# #Execice 2
# #Instructions
# #Write a function that accepts one parameter (an int: x) and returns the value of x+xx+xxx+xxxx.
def function_2(x):
    x = str(x)       
    total = int(x) + int(x*2) + int(x*3) + int(x*4)
    return total

print(function_2(2))
# #Execice 3
# #Instructions
import random
def throw_dice():
    return random.randint(1, 6)
def throw_until_doubles():
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        if dice1 == dice2:
            break
    return count
def main():
    results = [] 
    for i in range(100):
        throws = throw_until_doubles()
        results.append(throws)
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()


