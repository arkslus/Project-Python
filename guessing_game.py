# Guessing game
# A simple guessing game where the user has to guess a number between 1 and 100
import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0 # Number of attempts the user has to guess the number
max_attempts = 10 # Default number of attempts

# Display game information and rules
print("====================================")
print("Welcome to the Guessing Game!\nGood luck!")
print("====================================")
print("I have selected a secret number between 1 and 100.")
print("Guess the secret number between 1 and 100")

# Chose difficulty level
difficulty = input("Choose a difficulty level. Type 'easy', 'medium' or 'hard': ").lower()
if difficulty == 'easy':
    max_attempts = 10
    print("You have 10 attempts to guess the number.")
elif difficulty == 'medium':
    max_attempts = 7
    print("You have 7 attempts to guess the number.")
elif difficulty == 'hard':
    max_attempts = 5
    print("You have 5 attempts to guess the number.")
else:
    print("Invalid input. Defaulting to easy mode.")
    max_attempts = 10 


# Start the guessing game
print("====================================")
while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        break
    print("====================================")
else:
    print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")
    print("Better luck next time!")
