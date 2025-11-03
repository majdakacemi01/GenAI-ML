# #Exercise 1 : Use the terminal
# #Instructions
# #Run this command in the terminal to open a python console:
# #$ python3
# #Hint: Replace python3 with python for Windows
# #Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory

#You can run python in the terminal from any directory because the PATH environment variable tells the operating system where to look for executable programs. During installation, Python adds its directory to PATH, so when you type python3, the system searches the directories in PATH, finds the Python executable, and runs it—even if you are not in the Python installation folder.

# #Exercise 2 : Alias
# #Instructions
# #Read about alias, and try to open a python console with the command:
# #$ py
#Reponse:
#to create an alias in windows we can use the doskey command :
#doskey py=python

# #Exercise 3 : Outputs
# #Instructions
# #Predict the output of the following code snippets:

# #  1.  >>> 3 <= 3 < 9
# #  2.  >>> 3 == 3 == 3
# #  3.  >>> bool(0)
# #  4.  >>> bool(5 == "5")
# #  5. >>> bool(4 == 4) == bool("4" == "4")
# #  6.  >>> bool(bool(None))
# #  7. x = (1 == True)
# #    y = (1 == False)
# #    a = True + 4
# #    b = False + 10

# #    print("x is", x)
# #    print("y is", y)
# #    print("a:", a)
# #    print("b:", b)
#For 1. I guess True
#For 2. I guess True
#For 3. I guess False
#For 4. I guess False
#For 5. I guess True
#For 6. I guess False
#For 7. I guess x is True
#               y is False
#               a: 5
#               b: 10

# #Exercise 4 : How many characters in a sentence ?
# #Instructions
# #Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).

# #my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
# #           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
# #           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
# #           laboris nisi ut aliquip ex ea commodo consequat. 
# #           Duis aute irure dolor in reprehenderit in voluptate velit 
# #           esse cillum dolore eu fugiat nulla pariatur. 
# #           Excepteur sint occaecat cupidatat non proident, 
# #           sunt in culpa qui officia deserunt mollit anim id est laborum.
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text))
# #Exercise 5 : Longest word without a specific character
# #Instructions
# #1.Keep asking the user to input the longest sentence they can without the character “A”.
# #2.Each time a user successfully sets a new longest sentence, print a congratulations message.
# Initialize variable to keep track of the longest sentence
longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the letter 'A': ")
    if "a" in sentence.lower():
        print("Oops! Your sentence contains the letter 'A'. Try again.")
        continue
    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You set a new record for the longest sentence without 'A'!")
    else:
        print("Keep trying to beat your longest sentence!")