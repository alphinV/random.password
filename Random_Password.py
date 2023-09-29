import random
import string

randomno1 = str(random.randrange(1,99))

randomno2 = str(random.randrange(1,99))

# Define a list of special characters you want to use
special_characters = ['!', '@', '#', '$', '%', '^']

# Generate a random special character
random_character = str(random.choice(special_characters))

# Take user input for the keyword
keyword = input("Enter a keyword: ")

# Generate and print the password
password = keyword + randomno1 + randomno2 + random_character

print(password)
