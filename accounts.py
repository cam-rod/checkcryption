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

    data['user'] = input('\nPlease enter a username: ')
    data['pass'] = password_entry()

    en_user = Crypter(data['pass'], data['user']) # Crypter object to create encrypted username
    en_user.encryption_key = True # Generate encryption key
    data['e_user'] = en_user.encrypter # Encrypt the username

    del en_user
    return data # Both usernames and the password

def main():
    """This is the main process that determines whether to sign in or to create an account, and does such."""
    password = None
    while True:
        print('\nWould you like to create an account or sign in to your account?')
        print('Note: an account is required to encrypt or decrypt data.\n')
        option = input('Type \"1\" to create an account or \"2\" to sign in: ')
        if option != ('1' or '2'):
            print('\nSorry, that\'s not a valid option. Please try again.')
            continue # Reattempt option selection
        
        if option == '1': # Create account
            print('\nCreate your account here.')
            data = user_entry() # Get username and password
            print('\nCreating account...')
            write_users(data['user'], data['e_user']) # Write account details to users.txt

            del data
            print('Account created! Please sign in to continue.')
            continue
        else: # Sign in
            print('\nSign in here.')
            data = user_entry() # Get username and password
            print('\nSigning in...')
            saved = read_users()

            print('Verifying...')
            if (data['user'] == saved['user']) && (data['e_user'] == saved['e_user']): # Correct password entered
                password = data['pass']
                del data
                del saved
                print('You\'ve been signed in!')
                break
            else:
                del data
                del saved
                print('Sign in failed due to incorrect password. Please try again.')
                continue
    return password