"""This module hosts the menus for the checkcryption.py main program."""

import re
from crypterCore import accounts
from crypterCore.crypter import Crypter # encrypts and decrypts files and text
from crypterCore.data_parser import read_data, data_binary, write_data # Reads and writes text

def file_location():
    """This function requests a file location from the user."""

    while True:
        print('\nPlease enter the COMPLETE location of your file in one of these formats:')
        try:
            location = input('C:\\\\Users\\\\Admin\\\\file.txt OR C:/Users/Admin/file.txt: ')
            break
        except SyntaxError: # Used C:\ instead of C:\\ or C:/
            print('Entry failed, please use the correct format!')
            continue
    return location
    

def source_menu(option):
    """This function requests and returns the source data.

    The variable option alters how the question is posed and how the data is processed."""

    source_location = None # so it can be returned if it is not used

    if option == 'v':
        question = 'unencrypted data you would like to be verified'
    elif option == 'e':
        question = 'data you would like to be encrypted'
    else:
        question = 'data that has been encrypted' 

    while True:
        print('\nWhere is the {}?'.format(question))
        source_type = input('Press \'1\' to use a file, or \'2\' to directly input the text. ')

        if source_type == '1':
            while True:
                source_location = file_location()
                if option == 'e' or option == 'v': # To be encrypted
                    source = read_data(source_location, True)
                else: # To be verified
                    source = read_data(source_location, None, True)

                if source is None: # Invalid format
                    print('Entry failed, please use the correct format!')
                    continue
                else:
                    break 
            break
            
        elif source_type == '2':
            try:
                while True:  # Type source data
                    print('\nPlease enter your text here. To start a new line, type \\n.')
                    print('This field supports all letters, numbers, forward slash (/),')
                    print('and \\n specifically (no other symbols allowed). To go back to file')
                    print('selection, press Ctrl+Z and hit Enter.\n')
                    try:
                        source = input()
                        if re.search(r'[^A-Za-z0-9/ \n]', source): # invalid character
                            print('Entry failed, please use only the allowed characters!')
                            continue
                        else:
                            if option == 'e' or option == 'v': # To be encrypted
                                source = data_binary(source, True)
                            else:
                                source = data_binary(source, None)
                            break
                    except SyntaxError:
                        print('Entry failed, please use only the allowed characters!')
                        continue
                break
            except (KeyboardInterrupt, EOFError):
                continue
        else:
            print('That is not an option, please try again.')
            continue
    return [source, source_location]

def dest_menu(option, *source_location):
    """This function returns the destination file's location, or the encrypted data for verifying.
    
    The variable source_location is only used if it will overwrite the source file (encryption)."""

    if option == 'e': # Encryption
        while True:
            print("\nWhere would you like your data to be saved?")
            print("Press \'1\' to overwrite the current file, \'2\' to create a new file,")
            dest_type = input('or \'3\' to directly output to the command line. ')

            if dest_type == '1': # Overwrite file
                if source_location is None:
                    print('You did not provide a source file, please choose another option.')
                    continue
                else:
                    dest = source_location
                    break
            elif dest_type == '2': # Create a new file
                dest = file_location()
                break
            elif dest_type == '3': # Print to command line
                dest = None
                break
            else:
                print('That is not an option, please try again.')
                continue
        return dest
    else: # Verification
        final = source_menu('d')
        return final[0]

def verify_menu(source, dest, E_USER, process):
    """This menu verifies the user, and then runs the encryption/verification."""

    for attempt in range(6): # 3 password attempts, arbitrary number used
        attempt += 1
        if attempt > 3:
            print("All attempts used, please start again.")
            del source, dest, verify
            break
        print('\nPlease confirm your credentials (attempt {} of 3): '.format(attempt))
        verify = accounts.main('verify')
        if verify['e_user'] == E_USER: # Retrieved info matches signed in user
            print('Generating encryption key...')
            processing = Crypter(verify['pass'], source)
            processing.encryption_key = True

            if process == 'e': # Encrypt
                print('Encrypting data...')
                write_data(processing.encrypter(), dest)
                if dest is None:
                    print('Done!')
                else:
                    print('Done! Check {} to see your encrypted file.'.format(dest))
            else: # Verify
                print('Verifying...\n')
                e_source = processing.encrypter() # Encrypted source file
                if e_source == dest: # This is the original file
                    print('You have obtained the original file.')
                else:
                    print('====================================================')
                    print('WARNING: THIS IS NOT THE ORIGINAL FILE! BE CAREFUL!')
                    print('====================================================')
                    print('You have either used the wrong account or obtained the wrong file.')
            del source, dest, processing, verify
            break
        else:
            print('That is not the correct password.')

def main(E_USER):
    """This is the main menu of Checkcryption.
    
    E_USER: the encrypted username, used for verification."""

    while True: # The 'crypter' loop
        print('\nWhat would you like to do?')
        option = input('Type \'e\' to encrypt, \'v\' to verify, or \'q\' to quit: ')

        if re.match('e', option.lower()): # encrypt data
            print('\nEncryption menu:')

            source, source_location = source_menu('e') # Get source data

            dest = dest_menu('e', source_location) # Get destination location
            del source_location
            
            verify_menu(source, dest, E_USER, 'e') # Verify user and encrypt

            continue
        elif re.match('v', option.lower()): # decrypt data
            print('\nVerification menu:')

            source, source_location = source_menu('v') # Get source data
            dest = dest_menu('v') # Get encrypted data
            del source_location

            verify_menu(source, dest, E_USER, 'v') # Verify user and decrypt

            continue
        elif re.match('q', option.lower()): # quit
            break
        else:
            print('\nThat is not a valid option, please try again.')
            continue
    del E_USER
