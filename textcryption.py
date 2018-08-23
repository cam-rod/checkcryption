"""This is the main module of Textcryption.

This module introduces the program to the user and calls other module to carry out specific actions.
The module also acts a the main menu."""

import re
import accounts # Account creation or sign in
from crypter import Crypter # encrypts and decrypts files and text
from text_parser import read_text, text_to_binary, write_text # Reads and writes text

print("Welcome to Textcryption, the program that helps you protect your data!")

PASSWORD = accounts.main() # Signs in user

while True: # The 'crypter' loop
    if PASSWORD == None: # User opted to quit from signin menu
        break

    print('\nWhat would you like to do?')
    option = input('Type \'e\' to encrypt, \'d\' to decrypt, or \'q\' to quit: ')

    if re.match('e', option.lower()): # encrypt data
        pass
    elif re.match('d', option.lower()): # decrypt data
        pass
    elif re.match('q', option.lower()): # quit
        break
    else:
        print('\nThat is not a valid option, please try again.')
        continue
print('\nThank you for using Textcryption!')