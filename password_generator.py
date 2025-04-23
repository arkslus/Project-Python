# password generator program in Python
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
# Ask the user for the desired length of the password
num_of_letters = int(input("How many letters would you like in your password?\n"))
# ask the user for desired number of symbols
num_of_symbols = int(input(f"How many symbols would you like?\n"))
# ask the user for desired number of numbers
num_of_numbers = int(input(f"How many numbers would you like?\n"))
# ask the user for their desired password length.
# length = int(input("Enter the desired length of the password: "))

password = []

# generate random letters
for char in range(num_of_letters):
    password.append(random.choice(letters))

# generate random symbols
for char in range(num_of_symbols):
    password.append(random.choice(symbols))

# generate random numbers
for char in range(num_of_numbers):
    password.append(random.choice(numbers))

# shuffle the characters in the password
random.shuffle(password)

# join the characters to form the password
password = "".join(password)

print("________________________________")
# print the generated password
print(f"\nYour password is: {password}")
print("________________________________")