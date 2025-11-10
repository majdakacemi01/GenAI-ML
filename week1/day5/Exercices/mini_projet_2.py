import random
wordslist = [
    'correction', 'childish', 'beach', 'python', 'assertive',
    'interference', 'complete', 'share', 'credit card', 'rush', 'south'
]

word = random.choice(wordslist).lower()
guessed_letters = []           
lives = 6                      
display = ""                   
for letter in word:
    if letter == " ":
        display += " "         
    else:
        display += "*"         

print("Welcome to Hangman!")
print("Guess the word letter by letter.")
print("You have 6 lives. Good luck!\n")
while lives > 0 and "*" in display:
    print("Word:", display)
    print("Lives left:", lives)
    print("Guessed letters:", guessed_letters)
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter!\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

  
    guessed_letters.append(guess)
    if guess in word:
        print("Correct!\n")
        new_display = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_display += guess
            else:
                new_display += display[i]
        display = new_display
    else:
        print("Wrong guess!\n")
        lives -= 1

if "*" not in display:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Game Over! The word was: {word}")
