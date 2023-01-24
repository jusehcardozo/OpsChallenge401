#!/usr/bin/env python3

# Script: Ops 401 Challenge 06
# Author: Jose Cardozo
# Date of latest version:  01/23/2023
# Purpose: File Encryption Script Part 1 of 3

# Import Libraries

from cryptography.fernet import Fernet

# Function that generates a key
def write_key():
    # Generates a key and save it into a file
    
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Function that loads the generated key
def load_key():
    # Loads the key from the current directory named `key.key`
    
    return open("key.key", "rb").read()



# Function that encrypts a message
def encrypt_message():
    encrypted = f.encrypt(message)
    # print how it looks
    print(encrypted)

# Function that decrypts a message
def decrypt_message():
    decrypted_encrypted = f.decrypt(encrypted)
    print(decrypted_encrypted)


# Function that encrypts a file
def encrypt_file(filename, key):
    # Given a filename (str) and key (bytes), it encrypts the file and write it
    f = Fernet(key)


# Function that decrypts a file
def decrypt_file(filename, key):

    # Given a filename (str) and key (bytes), it decrypts the file and write it
   
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


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
    



# Infinite loop for user menu
# USE CONTROL C TO EXIT LOOP!!!
while True:
    ask_user()