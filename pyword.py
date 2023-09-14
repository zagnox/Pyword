import random
import string


def generate_password(length, numbers=True, symbols=True):

    #Defining variables for letters, numbers and special characters
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    passwd = ""

    #include digits to characters if numbers is set to True
    if numbers:
        characters += digits
    
    #include symbols to characters if symbols is set to True
    if symbols:
        characters += specials

    #generate a random password from characters
    for i in range(length):
        passwd += random.choice(characters)
    return passwd


#gathering user input for password strength
length = int(input("Enter your password length: "))
numbers = input("Do you want your new password to contain numbers? Y/n ").lower() == "y"
symbols = input("Do you want your new password to contain special characters? Y/n ").lower() == "y"

#assigning function output to varible
passwd = generate_password(length, numbers, symbols)

#printing out the password to user
print(f"Your new password is {passwd}")