"""This module interprets text from various sources.

Functions:
    - Gets and verifies a valid password for signing in.
    - Reads text from regular files or direct entry and converts to binary.
    - Writes encrypted text to files.
    - Reads and returns matching section from users.txt.
    - Writes usernames to users.txt."""

import re

def password_entry():
    """This function is called by accounts.user_entry() to get the password.
  
    It requests a password, checks to see if the password is valid, and if so returns the password."""
    password = None
    while True:
        print('\nPassword requirements:')
        print('  - Valid character are numbers, letters, and symbols ()[]!@#,.*/')
        print('  - The password must be EXACTLY 12 characters long')
        print('  - The password must include at least one lowercase letter, one uppercase letter,')
        print('    one number, and one symbol.\n')
        password = input('Please enter your password: ')

        if len(password) == 12:
            if re.search(r'^[A-Za-z0-9()[\]!@#,.*/]*$', password): # only valid characters used
                if (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', passsword)
                and re.search(r'[()[\]!@#,.*/]', password)): # minimum character requirements
                    break
                else:
                    print('That is not a valid password. Reason: password did not meet minimum requirements.')
                    continue
            else:
                print('That is not a valid password. Reason: invalid characters used in password.')
                continue
        else:
            print('That is not a valid password. Reason: password was not 12 characters long.')
            continue
    return password

def read_users(username):
    """This function checks if a username is found in users.txt and returns it if so."""
    print('Retriving user data...')
    saved_data = {}
    while True:
        with open('users.txt') as file:
            file_text = file.read() # get saved data
            located_data = re.search(username, file_text) # find the username
            try:
                
            except:
                break
    
    return saved_data

def write_users(user, e_user):
    print('Saving account details...')
    pass