"""This module interprets text from various sources.

Functions:
    - Gets and verifies a valid password for signing in.
    - Reads text from regular files or direct entry and returns it.
    - Converts text to binary.
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

def read_text(content, binary):
    """This function reads the content of a text file or direct entry.

    If requested, the text is then converted to binary before being returned."""
    pass

def text_to_binary(content):
    """This function converts UTF-8 text to binary."""
    pass

def write_text(content, destination):
    """This function writes encrypted text to the requested destination."""
    pass

def read_users(username):
    """This function checks if a username is found in users.txt and returns it if so.
    
    The returned data is in the form of a dictionary containing \'user\' and \'e_user\'."""
    print('Retriving user data...')
    saved_data = {}
    while True:
        with open('users.txt', 'r+') as file:
            file_text = file.read() # get saved data
            located_data = re.search(username, file_text) # find the username
            try:
                saved_data['user'] = file_text[located_data.start():located_data.end()] # Within the calculated span
                saved_data['e_user'] = file_text[(located_data.end())+1:(re.search(';',file_text[located_data.end()+1:]))]
                # From 1 char after user (semicolon) to the following semicolon
                break
            except:
                break
    
    del file_text
    del located_data
    return saved_data

def write_users(user, e_user):
    print('Saving account details...')
    successful = False
    while True:
        with open('users.txt', 'a+') as file:
            file.seek(0,0) # Go to start of file
            list_all = file.read()
            if re.search(user, list_all): # username is already taken
                break # failed setup
            else:
                file.seek(0,2)
                f.write('{};{};\n'.format(user, e_user)) # write usernames to a new line
                successful = True
                break
    
    del file
    del list_all
    return successful