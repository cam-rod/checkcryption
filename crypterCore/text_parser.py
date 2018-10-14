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

def text_binary(content, binary):
    """This function converts UTF-8 text to binary or vice versa.

    If binary is True, the text will be converted to binary; if False, from binary; if write,
    nothing occurs; if None, the text is split."""
    new_content = [] # Converted content
    e_content = [] # Content in encryption form ready to be returned

    if binary == 'write':
        return content
    elif binary is None:
        new_content = content.split('/')
        return [int(p) for p in new_content]
    elif binary:
        for char in content:
            char_array = '/'.join(map(bin, bytearray(char, 'utf8'))).split('/') # Extract all bytes
            
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
    elif binary is False:
        content = [str(i) for i in content]
        new_content = ''
        twofind = lambda c: re.search('2', content[c][seek+1:]) # Return location of 2 in content

        for c in range(len(content)): # Character pairs
            seek = 0 # ID's what has already been extracted
            while True: # Individual characters in pair
                try:
                    char = content[c][seek+1:twofind(c).start()+1] # From after 2 to before next 2
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

    if destination is None: # Command line output
        print('')
        print(content)
    else:
        with open(destination, 'w+') as file:
            print('\nWriting text to file...')
            file.write(content)
            print('Successful!')
