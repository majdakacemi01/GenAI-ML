# #Exercice 1
# #Instructions
# #Write a program that calculates and prints a value according to this given formula:
# #Q = Square root of [(2 * C * D)/H]
# #Following are the fixed values of C and H:
# #C is 50 and H is 30.
# #Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
C = 50
H = 30
list_Q = []
number = input('Enter numbers separated by commas: ')
numbers = number.split(",")
for n in numbers:
    D = int(n)
    Q = ((2 * C * D) / H) ** 0.5
    list_Q.append(Q)
print(list_Q)

# #Exercice 2
# #Instructions
# #Given a list of 10 integers to analyze
# #[44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
# #1. Store the list of numbers in a variable.
numbers = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
# #2. Print the following information:
# #a. The list of numbers – printed in a single line
print('List of numbers:', numbers)
# #b. The list of numbers – sorted in descending order (largest to smallest)
print('Descending order:', sorted(numbers, reverse=True))
# #c. The sum of all the numbers
print('Sum of all numbers:', sum(numbers))
# #3. A list containing the first and the last numbers.
list_1=[]
list_1.append(numbers[0])
list_1.append(numbers[-1])
print(list_1)
# #4. A list of all the numbers greater than 50.
list_2=[]
for n in numbers :
    if n > 50:
        list_2.append(n)
print(list_2)
# #5. A list of all the numbers smaller than 10.
list_3=[]
for n in numbers :
    if n < 10:
        list_3.append(n)
print(list_3)
# #6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
list_4=[]
for n in numbers:
    number_squared = n ** 2
    list_4.append(number_squared)
print(list_4)
# #7. The numbers without any duplicates – also print how many numbers are in the new list.
unique_numbers = list(set(numbers))
print('Numbers without duplicates:', unique_numbers)
print('Count of unique numbers:', len(unique_numbers))
# #8. The average of all the numbers.
average = sum(numbers) / len(numbers)
print("Average of all numbers:", average)
# #9. The largest number.
print("Largest number:", max(numbers))
# #10.The smallest number.
print("Smallest number:", min(numbers))
# #11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
for n in numbers:
    manual_sum += n
    if n > manual_max:
        manual_max = n
    if n < manual_min:
        manual_min = n
manual_average = manual_sum / len(numbers)
print("Sum (manual):", manual_sum)
print("Average (manual):", manual_average)
print("Largest (manual):", manual_max)
print("Smallest (manual):", manual_min)
# #12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
user_numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1} between -100 and 100: "))
    user_numbers.append(num)
print("User numbers:", user_numbers)
# #13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(-100, 100))
print("Random numbers:", random_numbers)
# #14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
amount = random.randint(50, 100)
random_list = []
for i in range(amount):
    random_list.append(random.randint(-100, 100))
print(f"\nGenerated {amount} random numbers between -100 and 100.")
print("Example list (first 10 shown):", random_list[:10])
# #15. Bonus: Will the code work when the number of random numbers is not equal to 10?
# yes, because we used len(random_list) when calculating things like averages,the code adapts automatically to any list size.
# #Exercice 3
# #Instructions
paragraph = "We learn Python for machine learning in Geeks Institute bootcamp."
num_characters = len(paragraph)
print("Number of characters:", num_characters)
sentences = paragraph.split(".")
# remove empty strings caused by trailing periods
sentences = [s for s in sentences if s.strip() != ""]
print("Number of sentences:", len(sentences))
words = paragraph.split()  # splits by spaces
print("Number of words:", len(words))
unique_words = set(words)
print("Number of unique words:", len(unique_words))
non_whitespace_chars = len(paragraph.replace(" ", "").replace("\n", ""))
print("Non-whitespace characters:", non_whitespace_chars)
average_words_per_sentence = len(words) / len(sentences)
print("Average words per sentence:", average_words_per_sentence)
from collections import Counter

word_counts = Counter(words)
non_unique_words = sum(count - 1 for count in word_counts.values() if count > 1)
print("Number of non-unique words:", non_unique_words)
# #Exercice 4
# #Instructions
# #Write a program that prints the frequency of the words from the input
text = input("Enter a paragraph: ")
words = text.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
for word, count in frequency.items():
    print(f"{word}:{count}")
