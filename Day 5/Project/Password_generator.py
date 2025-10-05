import string
import random


print('\nWelcome to the PyPassword Generator!')


# Create lists of possible characters for the password
letters = list(string.ascii_letters)      # All uppercase and lowercase letters
symbols = list(string.punctuation)        # All punctuation symbols
numbers = list(string.digits)             # All digits 0-9

# Ask the user for the number of each type of character
p_letters = int(input('\nHow many letters would you like in your password? '))
p_symbols = int(input('How many symbols would you like in your password? '))
p_numbers = int(input('How many numbers would you like in your password? '))

password = ''  # Initialize the password string

# Add random letters to the password
for char in range(1, p_letters + 1):
    password += random.choice(letters)
# Add random symbols to the password
for char in range(1, p_symbols + 1):
    password += random.choice(symbols)
# Add random numbers to the password
for char in range(1, p_numbers + 1):
    password += random.choice(numbers)
    
# Shuffle the password to randomise the character order
password = list(password)
random.shuffle(password)
password = ''.join(password)

print(f'\nYour new password is: {password}\n')
