"""This module hosts the menus for the textcryption.py main program."""

import re
from crypterCore import accounts
from crypterCore.crypter import Crypter # encrypts and decrypts files and text
from crypterCore.text_parser import read_text, text_binary, write_text # Reads and writes text

def file_location(*purpose):
    """This function requests a file location from the user.

    The variable purpose (optional) specify whether it is a source or destination file location."""

    while True:
        print('\nPlease enter the COMPLETE location of your .txt file in one of these formats:')
        try:
            location = input('C:\\\\Users\\\\Admin\\\\file.txt OR C:/Users/Admin/file.txt:')

            if not re.search('.txt$', location): # Only .txt files allowed
                print('That is not a .txt file, please try again.')
                continue

            if purpose == 's': # Get source data
                source = read_text(location, True)

                if source == FileNotFoundError: # Invalid format
                    print('Entry failed, please use the correct format!')
                    continue
            break
        except SyntaxError: # Used C:\ instead of C:\\ or C:/
            print('Entry failed, please use the correct format!')
            continue
    if purpose == 's':
        return [source, location]
    else:
        return location
    

def source_menu(option):
    """This function requests and returns the source data.

    The variable option alters how the question is posed."""

    source_location = None # so it can be returned if it is not used

    question = 'decrypted' if option == 'd' else 'encrypted' # Modifies question

    while True:
        print('\nWhere is the data you would like to be {}?'.format(question))
        source_type = input('Press \'1\' to use a file, or \'2\' to directly input the text.')

        if source_type == '1':
            source, source_location = file_location('s')
            
        elif source_type == '2':
            while True:  # Type source data
                print('\nPlease enter your text here. To start a new line, use \\n in the line.')
                print('This field support all uppercase and lowercase letters, numbers, and \\n specifically (no symbols).')
                try:
                    source = input()
                    if re.search(r'[^A-Za-z0-9 \n]', source): # invalid character
                        print('Entry failed, please use only the allowed characters!')
                        continue
                    else:
                        source = text_binary(source, True)
                        break
                except SyntaxError:
                    print('Entry failed, please use only the allowed characters!')
                    continue
        else:
            print('That is not an option, please try again.')
            continue
    return [source, source_location]

def dest_menu(source_location):
    """This function requests the output location of the data.
    
    The variable source_location is only used if it will overwrite the source file."""

    while True:
        print("\nWhere would you like your data to be saved?")
        print("Press \'1\' to overwrite the current file, \'2\' to create a new file,")
        dest_type = input('or \'3\' to directly output to the command line.')

        if dest_type == '1': # Overwrite file
            if source_location == None:
                print('You did not provide a source file, please choose another option.')
                continue
            else:
                dest = source_location
                break
        elif dest_type == '2': # Create a new file
            dest = file_location()
        elif dest_type == '3': # Print to command line
            dest = None
            break
        else:
            print('That is not an option, please try again.')
            continue
    return dest

def verify_menu(source, dest, E_USER):
    """This menu verifies that the user is who they say they are, and then runs the encryption/decryption."""

    for attempt in range(6): # 3 password attempts, arbitrary number used
        attempt += 1
        if attempt > 3:
            print("All attempts used, please start again.")
            del source, dest, verify
            break
        print('\nPlease confirm your identity (attempt {} of 3): '.format(attempt))
        verify = accounts.user_entry()
        if verify['e_user'] == E_USER: # Retrieved info matches signed in user
            print('Generating encryption key...')
            processing = Crypter(verify['pass'], source)
            processing.encryption_key = True

            print('Decrypting text...')
            write_text(processing.encrypter(), dest, None)
            print('Done! Check {} to see your encrypted file.'.format(dest))
            del source, dest, processing, verify
            continue
        else:
            print('That is not the correct password.')

def main(E_USER):
    """This is the main menu of Textcryption.
    
    E_USER: the encrypted username, used for verification."""

    while True: # The 'crypter' loop
        if E_USER == None: # User opted to quit from signin menu
            break

        print('\nWhat would you like to do?')
        option = input('Type \'e\' to encrypt, \'d\' to decrypt, or \'q\' to quit: ')

        if re.match('e', option.lower()): # encrypt data
            print('\nEncryption menu:')

            source, source_location = source_menu('e') # Get source data
            dest = dest_menu(source_location) # Get destination location
            del source_location
            
            verify_menu(source, dest, E_USER) # Verify user and encrypt

            continue
        elif re.match('d', option.lower()): # decrypt data
            print('\nDecryption menu:')

            source, source_location = source_menu('d') # Get source data
            dest = dest_menu(source_location) # Get destination location
            del source_location

            verify_menu(source, dest, E_USER) # Verify user and decrypt

            continue
        elif re.match('q', option.lower()): # quit
            break
        else:
            print('\nThat is not a valid option, please try again.')
            continue
    del E_USER