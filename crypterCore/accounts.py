"""This module handles the creation of new accounts and signing into old accounts.

Arguments: None

Functions:
    - main loop for what the user wants to do.
        - creates an account and adds usernames to users.txt.
        - signs in using data from users.txt.
    - requests and returns the entered username, encrypted username, and password."""

from checkcryption.checkcryption import Outline # GUI
from crypterCore.data_parser import password_entry, data_binary
from crypterCore.crypter import Crypter

def main(*choice):
    """This function requests a username and password and returns the encrypted username.
    
    choice (optional): used for introductory message or verification"""
    data = {'user': None, 'pass': None, 'e_user': None} # e_user is the encrypted username

    try:
        try:
            if choice[0] == 'setup': # Beginning of program
                print('Sign in or create your Checkcryption account.')
        except IndexError:
            pass
        data['user'] = input('\nPlease enter a username (to quit, press Ctrl+Z and hit Enter): ')
        data['pass'] = password_entry()

        data['user'] = data_binary(data['user'], True)
        user = data['user'] # Separate storage
        user = ''.join([str(i) for i in user])

        en_user = Crypter(data['pass'], data['user']) # Crypter object to create encrypted username
        en_user.encryption_key = True # Generate encryption key
        data['e_user'] = en_user.encrypter() # Encrypt the username

        data['user'] = user
        del en_user, user

        try:
            if choice[0] == 'verify':
                return data
            else:
                return data['e_user'] # Encrypted username
        except IndexError:
            return data['e_user'] # Encrypted username
    except (KeyboardInterrupt, EOFError):
        return
