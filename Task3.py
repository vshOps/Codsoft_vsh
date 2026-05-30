# PASSWORD GENERATOR PROJECT

# Import random module
import random

# Import string module
import string

# Ask user for password length
length = int(input("Enter password length: "))

# Store all possible characters
characters = "abcdefghijklmnopqrstuvwxyz" + "1234567890" + "\!@#%&" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Generate random password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display generated password
print("\nGenerated Password:")
print(password)