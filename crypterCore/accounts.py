"""This module handles the creation of new accounts and signing into old accounts.

Arguments: None

Functions:
    - main loop for what the user wants to do.
        - creates an account and adds usernames to users.txt.
        - signs in using data from users.txt.
    - requests and returns the entered username, encrypted username, and password."""

import re
from crypterCore.text_parser import password_entry, read_users, write_users, text_binary
from crypterCore.crypter import Crypter

def user_entry():
    """This function requests username and password and returns them and the encrypted username."""
    data = {'user': None, 'pass': None, 'e_user': None} # e_user is the encrypted username

    data['user'] = input('\nPlease enter a username: ')
    data['pass'] = password_entry()

    data['user'] = text_binary(data['user'], True)
    user = data['user'] # Separate storage
    user = ''.join([str(i) for i in user])

    en_user = Crypter(data['pass'], data['user']) # Crypter object to create encrypted username
    en_user.encryption_key = True # Generate encryption key
    data['e_user'] = en_user.encrypter() # Encrypt the username

    data['user'] = user
    del en_user, user
    return data # Both usernames and the password

def main():
    """This facilitates sign in or account creation."""
    e_user = None
    while True:
        print('\nWould you like to create an account or sign in to your account?')
        print('Note: an account is required to encrypt or decrypt data.\n')
        option = input('Type \'c\' to create an account, \'s\' to sign in, or \'q\' to quit'
                       + ' the program: ')
        
        if re.match('c', option.lower()): # Create account
            print('\nCreate your account here.')
            data = user_entry() # Get username and password
            print('\nCreating account...')
            successful = write_users(str(data['user']), data['e_user']) # Add account to users.txt

            if successful:
                del data
                del successful
                print('Account created! Please sign in to continue.')
                continue
            else:
                del data
                del successful
                print('This username already exists. Please try another one.')
                continue
        elif re.match('s', option.lower()): # Sign in
            print('\nSign in here.')
            data = user_entry() # Get username and password
            print('\nSigning in...')
            saved = read_users(data['user'])

            print('Verifying...')
            if saved == {}: # No such username found
                del data
                del saved
                print('No such username found. Please try again or create an account.')
                continue
            if ((str(data['user']) == saved['user'])
                    and (data['e_user'] == saved['e_user'])): # Correct password entered
                e_user = data['e_user']
                del data
                del saved
                print('You\'ve been signed in!')
                break
            else:
                del data
                del saved
                print('Sign in failed due to incorrect password. Please try again.')
                continue
        elif re.match('q', option.lower()): # quit program
            return 
        else:
            print('\nSorry, that\'s not a valid option. Please try again.')
            continue # Reattempt option selection
    return e_user
