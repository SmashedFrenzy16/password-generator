import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list("!£$%^&*()@#")

characters = (string.ascii_letters, string.digits, special_characters, "!£$%^&*()@#")

def random_password():

    total_length = int(input("Enter total password length: "))

    letters_count = int(input("Enter number of letters in password: "))
    numbers_count = int(input("Enter number of integers in password: "))
    special_count = int(input("Enter number of special characters in password: "))

    characters_count = letters_count + numbers_count + special_count

    if characters_count > total_length:
        print("The number of characters specified was longer than the total password length!")
        return
    
    password = []

    for i in range(letters_count):
        password.append(random.choice(letters))
    
    for i in range(numbers_count):
        password.append(random.choice(numbers))
    
    for i in range(special_count):
        password.append(random.choice(special_characters))
    
    if characters_count < total_length:
        password.append(random.choice(characters))
    
    random.shuffle(password)

    print("".join(password))

random_password()
