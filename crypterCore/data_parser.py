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
    """This function is called to validate and return a user's password."""
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
                print('\nThat is not a valid password. Reason: invalid characters used in'
                      + ' password.')
                continue
        else:
            print('\nThat is not a valid password. Reason: password was not 12 characters long.')
            continue
    return password

def data_binary(content, binary):
    """This function converts UTF-8 text to binary or vice versa.

    If binary is True, the text will be converted to binary; if False, from binary;
    if None, nothing happens."""
    new_content = [] # Converted content
    e_content = [] # Content in encryption form ready to be returned

    if binary is None:
        return content
    else:
        for char in content:
            char_array = '/'.join(map(bin, bytearray(str(char), 'utf8'))).split('/') # Extract bytes
            
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
                e_content.append(new_content[2*i] + new_content[(2*i)+1]
                                 + new_content[(2*i)+2]) # Combine a trio of chars
        except IndexError: # Always occurs
            # May combine last character with 2nd-4th last characters, this is intentional
            e_content.append(new_content[-1] + new_content[-2])
        finally:
            if len(new_content) % 3 == 0: # Multiple of 3 characters
                del e_content[-1] # Delete the repeated character
        
        return [int(c) for c in e_content] # Return list indexes as integers

def read_data(content, binary, *verify):
    """This function reads the content of a text file or direct entry.

    If requested, the text is then converted to binary before being returned.
    Encrypted files to be verified will be opened in non-binary read mode."""

    try:
        try:
            if verify[0]:
                with open(content) as file: # Non-binary read mode
                    source = file.read()
                source = data_binary(source, binary) # Convert to binary if requested
        except IndexError:    
            with open(content, 'rb') as file:
                source = file.read()
            source = data_binary(source, binary) # Convert to binary if requested

        return source
    except FileNotFoundError:
        return None

def write_data(content, destination):
    """This function writes text to the requested destination."""

    if destination is None: # Command line output
        print('')
        print(content)
    else:
        with open(destination, 'w+') as file:
            print('\nWriting text to file...')
            file.write(content)
            print('Successful!')
