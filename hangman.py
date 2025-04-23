# Hangman project

# import random
import random

# Set the number of lives the player starts with
lives = 6

# import the words list from hangman_word.py
from hangman_word import words

# import hangman_art
from hangman_art import stages, logo

# Print the ASCII art of the hangman
print(logo)

# select a random word from the list above
word = random.choice(words)
# print(f"The word you need to guess is: {word}")

# Create a "placeholder" with the same number of blanks as the chosen_word
blanks = "_" * len(word)
print(f"Current state of the word: {blanks}")

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# user_guessed = input("Guess a letter: ")

# set game over = False
game_over = False
correct_letters = []

# while the game is not over
while not game_over:
    # Print the ASCII art of the hangman with the current number of lives left.
    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    # display them all
    display = ""

    # Loop through each letter in the chosen_word.
    for letter in word:
        if letter.lower() == guess:
            display += letter
            correct_letters.append(letter.lower())
        elif letter.lower() in correct_letters:
            display += letter
        else:
            display += "_"
    # print the display
    print(f"Word to guess: {display}")

    # Check if the letter the user guessed (guess) is not in the chosen_word. If it is, decrease the number of lives by 1.
    if guess.lower() not in word:
        lives -= 1
        print(f"you guessed {guess} incorrectly. You have {lives} lives left.")
        # If the user has no lives left, end the game.
        if lives == 0:
            print("________________________________________________________________")
            print(f"Game Over! The word was {word}. You have lost!")
            print("________________________________________________________________")
            game_over = True

    # Check if the user has won by checking if all the letters in the chosen_word have been guessed.
    if "_" not in display:
        print("Congratulations! You've guessed the word!")
        game_over = True

    # print the stages of the game
    print("________________________________________________________________")
    print(stages[lives])
    print("________________________________________________________________")
