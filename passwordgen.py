# Random Password Generator (Beginner Friendly)
# This script creates a strong random password based on user input

import random   # Used to pick random characters
import string   # Contains ready-made character sets (letters, digits, symbols)

print("=== Random Password Generator ===\n")

# Ask user how long the password should be
length = int(input("Enter password length (e.g., 8, 12, 16): "))

# Ask user what to include in the password
use_letters = input("Include letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

# Start with an empty string that will hold all possible characters
characters = ""

# Add letters (both lowercase and uppercase)
if use_letters == 'y':
    characters += string.ascii_letters

# Add numbers (0–9)
if use_numbers == 'y':
    characters += string.digits

# Add symbols (like !@#$ etc.)
if use_symbols == 'y':
    characters += string.punctuation

# If user didn't choose anything, we stop the program
if characters == "":
    print("You must select at least one option!")
    exit()

# Now generate the password
password = ""

# Loop for the desired length
for i in range(length):
    # Pick a random character from the selected set
    password += random.choice(characters)

# Show the final password
print("\nYour generated password is:")
print(password)