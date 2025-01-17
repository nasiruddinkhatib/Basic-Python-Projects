import random  # Importing the 'random' module for random selection and shuffling

# Defining the character sets for password generation
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']  # List of lowercase and uppercase letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # List of digits 0-9
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  # List of common special characters
print("Welcome to Password Generator")  # Displaying a welcome message
# Asking the user how many of each type of character they want in their password
n_letter = int(input("How Many Letters You Want in Your Password?\n"))  # Number of letters
n_Symbols = int(input("How Many Symbols You Want in Your Password?\n"))  # Number of symbols
n_numbers = int(input("How Many Numbers You Want in Your Password?\n"))  # Number of numbers
# Initializing an empty list to hold the characters of the password
password_list = []
# Adding random letters to the password list
for i in range(1, n_letter + 1):  # Looping n_letter times
    char = random.choice(letters)  # Choosing a random letter from the letters list
    password_list += char  # Adding the chosen letter to the password list

# Adding random symbols to the password list
for i in range(1, n_Symbols + 1):  # Looping n_Symbols times
    char = random.choice(symbols)  # Choosing a random symbol from the symbols list
    password_list += char  # Adding the chosen symbol to the password list

# Adding random numbers to the password list
for i in range(1, n_numbers + 1):  # Looping n_numbers times
    char = random.choice(numbers)  # Choosing a random number from the numbers list
    password_list += char  # Adding the chosen number to the password list

# Printing the password list before shuffling (for debugging)
print(password_list)  # Shows the password characters in their original order

# Shuffling the characters in the password list to ensure randomness
random.shuffle(password_list)

# Printing the password list after shuffling (for debugging)
print(password_list)  # Shows the password characters after shuffling
# Combining the shuffled characters into a single string
password = ""  # Initializing an empty string for the final password
for char in password_list:  # Looping through each character in the shuffled password list
    password += char  # Adding each character to the password string
# Printing the final password
print(password)  # Displaying the generated password


#OUTPUT:
# Welcome to Password Generator
# ['a', 'B', 'z', 'P', '!', '$', '4', '7', '1']  #Characters before shuffle
# ['1', 'z', '$', '7', 'P', '!', 'a', 'B', '4']  # Characters after shuffle
# 1z$7P!aB4    Final password
