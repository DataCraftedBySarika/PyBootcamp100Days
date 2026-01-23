import random

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = [0,1,2,3,4,5,6,7,8,9]

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Ask user how many characters they want in their password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Empty list to store selected characters
password_list = []

# Add random letters to password_list
for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to password_list
for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers to password_list
for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the list so characters are in random order
random.shuffle(password_list)

# Convert list into a string
password = ''
for alphabet in password_list:
    password = password + str(alphabet)

# Display the final password
print(f"Here is your strong password: {password}")
