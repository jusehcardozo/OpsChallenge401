#!/usr/bin/env python3

# Script: Ops 401 Challenge 06
# Author: Jose Cardozo
# Date of latest version:  01/23/2023
# Purpose: File Encryption Script Part 1 of 3

# Import Libraries

from cryptography.fernet import Fernet
from os.path import exists

# Function that generates a key
def write_key():
    # Generates a key and save it into a file
    
    key = Fernet.generate_key()
    # Creates file key.key and saves the value into a file
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Function that loads the generated key
def load_key():
    # Loads the key from the current directory named `key.key`
    # Read method reads the content
    return open("key.key", "rb").read()



# Function that encrypts a message
def encrypt_message():
    user_message = input("What message would you like to Encrypt?")
    enconded_message = user_message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(enconded_message)
    print("This is the encrypted Message")
    # encrypted = f.encrypt(message)
    # print how it looks
    print(encrypted_message)

# Function that decrypts a message
def decrypt_message():
    user_message = input("What message would you like to encrypt")
    # Decodes the encrypted message provided by the user
    decoded_message = str.encoded(user_message)
    # Initialize Fernet class
    f = Fernet(key)
    # Decrypt the message
    decrypted_encrypted = f.decrypt(decoded_message)
    print("This is you decrypted message:")
    print(decrypted_encrypted)


# Function that encrypts a file
def encrypt_file():
    # Asking the full file path to be encrypted
    file_name = input("Enter the file path to be encrypted")
    # This opens the file and reads the contents
    with open(file_name, "rb") as file:
        # This reads the contents of the file and saves it in a variable called file_data
        file_data = file.read()

    # Initialize the Fernet class
    f = Fernet(key)

    # Encrypt the contents of the file and save in a variable called encrypted_file
    encrypted_file = f.encrypt(file_data)

    # Write the encrypted data to a file
    with open(file_name, "wb") as file:
        file.write(encrypted_file)


# Function that decrypts a file
def decrypt_file():

    # Ask the path to be decrypted
    file_name = input("Enter the file path to be decrypted")

    # This opens the file and reads the contents
    with open(file_name, "rb") as file:
        # This reads the contents of the file and saves it in a variable called file_data
        file_data = file.read()

        # Initialize the Fernet class
        f = Fernet(key)

        # Decrypt data
        decrypted_data = f.decrypt(file_data)

        # Write the decrypted data to a file
    with open(file_name, "wb") as file:
        file.write(decrypted_file)
    
   

# Function that gives a user a menu
def ask_user():
    mode = input("\nWhat would you like to do? \n1 - Encrypt a file \n2 - Decrypt a file \n3 - Encrypt a message \n4 - Decrypt a message")

    if (mode == "1"):
        encrypt_file()
        print("File Encrypted!")
    elif (mode == "2"):
        decrypt_file()
        print("File Decrypted!")
    elif (mode == "3"):
        encrypt_message()
        print("Message Encrypted!")
    elif (mode == 4):
        decrypt_message
        print("Message Decrypted!")
    elif ((mode != "1") and (mode != "2") and (mode != "3") and (mode != "4")):
        print("Wrong Choice! Choose again.")
    
key_exists = exists('./key.key')

# Check if the key file exists then call the load_key funtion to read it
if key_exists:
    key = load_key()
else:
    write_key()
    key = load_key()

# Infinite loop for user menu
# USE CONTROL C TO EXIT LOOP!!!
while True:
     ask_user()