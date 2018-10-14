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
    """This function is called by accounts.user_entry() to validate and return a user's password."""
    password = None
    while True:
        print('\nPassword requirements:')
        print('  - Valid character are numbers, letters, and symbols ()[]!@#,.*/')
        print('  - The password must be EXACTLY 12 characters long')
        print('  - The password must include at least one lowercase letter, one uppercase letter,')
        print('    one number, and one symbol.\n')
        password = input('Please enter your password: ')

        if len(password) == 12:
            if re.search(r'^[A-Za-z\d()[\]!@#,.*/]*$', password): # only valid characters used
                if (re.search(r'[A-Z]', password)
                        and re.search(r'[a-z]', password)
                        and re.search(r'[0-9]', password)
                        and re.search(r'[()[\]!@#,.*/]', password)):
                    break
                else:
                    print('\nThat is not a valid password.' +
                          'Reason: password did not meet minimum requirements.')
                    continue
            else:
                print('\nThat is not a valid password. Reason: invalid characters used in password.')
                continue
        else:
            print('\nThat is not a valid password. Reason: password was not 12 characters long.')
            continue
    return password

def text_binary(content, binary):
    """This function converts UTF-8 text to binary or vice versa.
    
    If binary is True, the text will be converted to binary; if False, from binary; if write, nothing occurs; if None,
    the text is split."""
    new_content = [] # Converted content
    e_content = [] # Content in encryption form ready to be returned

    if binary == 'write':
        return content
    if binary == None:
        new_content = content.split('/')
        return [int(p) for p in new_content]
    elif binary:
        for char in content:
            char_array = '/'.join(map(bin,bytearray(char, 'utf8'))).split('/') # Extract all bytes
            
            char_list = [] # Formatted text for appending
            for byte in char_array:
                # Split out the 'b' and only save the last 8 bits
                char_list.append(''.join(byte.split('b')[-8:]))
            
            # Remove extra characters for easy conversion with chr later
            if len(char_list) == 1:
                char_list[0] = char_list[0][-7:]
            elif len(char_list) == 2:
                char_list[0] = char_list[0][-5:]
                char_list[1] = char_list[0][-6:]
            elif len(char_list) == 3:
                char_list[0] = char_list[0][-4:]
                char_list[1] = char_list[1][-6:]
                char_list[2] = char_list[2][-6:]
            else:
                char_list[0] = char_list[0][-3:]
                char_list[1] = char_list[1][-6:]
                char_list[2] = char_list[2][-6:]
                char_list[3] = char_list[3][-6:]
            
            new_content.append('2'+''.join(char_list))
        try:
            for i in range(len(new_content)):
                e_content.append(new_content[2*i] + new_content[(2*i)+1]) # Combine a pair of characters
        except IndexError: # Always occurs
            e_content.append(new_content[-1])
        finally:
            if len(new_content) % 2 == 0: # Even number of characters
                del e_content[-1] # Delete the repeated character
        
        return [int(c) for c in e_content] # Return list indexes as integers
    elif binary == False:
        content = [str(i) for i in content]
        new_content = ''
        twofind = lambda c: re.search('2', content[c][seek+1:]) # Return the location of next 2 in content

        for c in range(len(content)): # Character pairs
            seek = 0 # ID's what has already been extracted
            while True: # Individual characters in pair
                try:
                    char = content[c][seek+1:twofind(c).start()+1] # From after the 2 to before the next one
                except AttributeError: # For second character (or last in whole text)
                    char = content[c][seek+1:]
                finally:
                    char = chr(int(char, 2)) # Convert to utf-8
                    new_content += char
                    try:
                        seek += twofind(c).start()+1
                        if seek == 0: # Loop completed
                            break
                    except AttributeError: # Loop completed by NoneType
                        break

        return new_content # For saving

def read_text(content, binary):
    """This function reads the content of a text file or direct entry.

    If requested, the text is then converted to binary before being returned."""

    try:
        with open(content) as file:
            source = file.read()
        source = text_binary(source, binary) # Convert to binary if requested

        return source
    except FileNotFoundError:
        return None

def write_text(content, destination, binary):
    """This function writes text to the requested destination.
    
    If requested, the text is then converted from binary before being written."""
    
    content = text_binary(content, binary) # Convert from binary if requested

    if destination == None: # Command line output
        print('')
        print(content)
    else:
        with open(destination, 'w+') as file:
            print('\nWriting text to file...')
            file.write(content)
            print('Successful!')

def read_users(username):
    """This function checks if a username is found in users.txt and returns it if so.
    The returned data is in the form of a dictionary containing \'user\' and \'e_user\'."""
    print('Retriving user data...')
    saved_data = {}
    while True:
        with open('users.txt', 'r+') as file:
            file_text = file.read() # get saved data
            located_data = re.search(str(username), file_text) # find the username
            try:
                # Within the calculated span
                saved_data['user'] = file_text[located_data.start():located_data.end()]
            except AttributeError:
                break
            try:
                # From 1 char after user (semicolon) to the following semicolon
                saved_data['e_user'] = file_text[(located_data.end())+1:
                                                 (re.search(';', file_text[located_data.end()+1:]).start())
                                                 +located_data.end()+1]
                break
            except TypeError:
                saved_data['user'] = None
                saved_data['e_user'] = None
                break
    del file_text
    del located_data
    return saved_data

def write_users(user, e_user):
    """This function writes user data to users.txt."""
    print('Saving account details...')
    successful = False
    while True:
        with open('users.txt', 'a+') as file:
            file.seek(0, 0) # Go to start of file
            list_all = file.read()
            if re.search(user, list_all): # username is already taken
                break # failed setup
            else:
                file.seek(0, 2)
                file.write('{};{};\n'.format(user, e_user)) # write usernames to a new line
                successful = True
                break
    del file
    del list_all
    return successful
