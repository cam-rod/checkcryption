"""This module handles the creation of new accounts and signing into old accounts.

Arguments: None

Functions:
    - main loop for what the user wants to do.
        - creates an account and adds usernames to users.txt.
        - signs in using data from users.txt.
    - requests and returns the entered username, encrypted username, and password.
"""
from text_parser import password_entry, read_users, write_users
from crypter import Crypter

def user_entry():
    """This function requests the username and password from the user and returns them and the encrypted username."""
    data = {'user': None, 'pass': None, 'e_user': None} # e_user is the encrypted username

    data['user'] = input("Please enter a username: ")
    data['pass'] = password_entry()

    en_user = Crypter(data['pass'], data['user']) # Crypter object to create encrypted username
    en_user.encryption_key = True # Generate encryption key
    data['e_user'] = en_user.encrypter # Encrypt the username

    del en_user
    return data # Both usernames and the password

def main():
    """This is the main process thee determines whether to sign in or to create an account, and does such."""
    pass
