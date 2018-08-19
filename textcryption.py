"""This is the main module of Textcryption.

This module introduces the program to the user and calls other module to carry out specific actions.
The module also acts a the main menu."""

import accounts # Account creation or sign in
from crypter import Crypter # encrypts and decrypts files and text
from text_parser import read_text, text_to_binary, write_text # Reads and writes text

print("Welcome to Textcryption, the program that helps you protect your data!")

PASSWORD = accounts.main() # Signs in user

while True: # The 'crypter' loop
    pass
