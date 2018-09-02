"""This is the main module of Textcryption.

This module introduces the program to the user and calls other module to carry out specific actions.
The module also acts a the main menu."""

import re
from crypterCore import accounts # Account creation or sign in
from crypterCore.crypter import Crypter # encrypts and decrypts files and text
from crypterCore.text_parser import read_text, text_binary, write_text # Reads and writes text

option = None # Encrypt, decrypt, or quit
source_type = None # Direct entry or file
dest_type = None # Direct entry or file
source = None # Source data 
dest = None #E  Exported data

print("Welcome to Textcryption, the program that helps you protect your data!")

E_USER = accounts.main() # Signs in user

while True: # The 'crypter' loop
    if E_USER == None: # User opted to quit from signin menu
        break

    print('\nWhat would you like to do?')
    option = input('Type \'e\' to encrypt, \'d\' to decrypt, or \'q\' to quit: ')

    if re.match('e', option.lower()): # encrypt data
        print('\nEncryption menu:')
        while True: # Source data
            print('\nHow would you like to select your data to be encrypted?')
            source_type = input('Press \'1\' to use a file, or \'2\' to directly input the text.')

            if source_type == '1':
                while True: # Location of source file
                    print('\nPlease enter the COMPLETE location of your file in one of these formats:')
                    try:
                        source_location = input('C:\\\\Users\\\\Admin\\\\file.txt OR C:/Users/Admin/file.txt: ')
                        source = read_text(source_location, True)

                        if source == FileNotFoundError: # Invalid format
                            print('Entry failed, please use the correct format!')
                            continue
                        break
                    except SyntaxError: # Used C:\ instead of C:\\ or C:/
                        print('Entry failed, please use the correct format!')
                        continue
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
        while True: # Destination
            print("\nWhere would you like your data to be saved?")
            print("Press \'1\' to overwrite the current file, \'2\' to create a new file,")
            dest_type = input('or \'3\' to directly output to the command line.')

            if dest_type == '1': # Overwrite file
                try:
                    dest = source_location
                    break
                except NameError:
                    print('You did not provide a source file, please choose another option.')
                    continue
            elif dest_type == '2': # Create a new file
                while True: # Location of source file
                    print('\nPlease enter the COMPLETE intended location of your destination in one of these formats:')
                    try:
                        dest = input('C:\\\\Users\\\\Admin\\\\new_file.txt OR C:/Users/Admin/new_file.txt: ')

                        try: # Check for valid filepath
                            with open(dest) as file:
                                tmp = 1
                                del tmp
                        except FileNotFoundError:
                            print('Entry failed, please use the correct format!')
                            continue
                        break
                    except SyntaxError: # Used C:\ instead of C:\\ or C:/
                        print('Entry failed, please use the correct format!')
                        continue 
            elif dest_type == '3': # Print to command line
                dest = None
                break
            else:
                print('That is not an option, please try again.')
                continue
        for attempt in range(6): # 3 password attempts, arbitrary number used
            attempt += 1
            if attempt > 3:
                print("All attempts used, please start again.")
                del source, source_location, source_type, dest, dest_type, verify
                break
            print('\nPlease confirm your identity (attempt {} of 3): '.format(attempt+1))
            verify = accounts.user_entry()
            if verify['e_user'] == E_USER:
                print('Generating encryption key...')
                processing = Crypter(verify['pass'], source)
                processing.encryption_key = True

                print('Decrypting text...')
                write_text(processing.encrypter(), dest, None)
                print('Done! Check {} to see your encrypted file.'.format(dest))
                del source, source_location, source_type, dest, dest_type, processing, verify
                continue
            else:
                print('That is not the correct password.')
        continue
    elif re.match('d', option.lower()): # decrypt data
        print('\nDecryption menu:')
        while True: # Source data
            print('\nHow would you like to select your data to be decrypted?')
            source_type = input('Press \'1\' to use a file, or \'2\' to directly input the text.')

            if source_type == '1':
                while True: # Location of source file
                    print('\nPlease enter the COMPLETE location of your file in one of these formats:')
                    try:
                        source_location = input('C:\\\\Users\\\\Admin\\\\file.txt OR C:/Users/Admin/file.txt: ')
                        source = read_text(source_location, None)
                        
                        if source == FileNotFoundError: # Invalid format
                            print('Entry failed, please use the correct format!')
                            continue
                        break
                    except SyntaxError: # Used C:\ instead of C:\\ or C:/
                        print('Entry failed, please use the correct format!')
                        continue
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
                            source = text_binary(source, None)
                            break
                    except SyntaxError:
                        print('Entry failed, please use only the allowed characters!')
                        continue
            else:
                print('That is not an option, please try again.')
                continue
        while True: # Destination
            print("\nWhere would you like your data to be saved?")
            print("Press \'1\' to overwrite the current file, \'2\' to create a new file,")
            dest_type = input('or \'3\' to directly output to the command line.')

            if dest_type == '1': # Overwrite file
                try:
                    dest = source_location
                except NameError:
                    print('You did not provide a source file, please choose another option.')
                    continue
                break
            elif dest_type == '2': # Create a new file
                while True: # Location of source file
                    print('\nPlease enter the COMPLETE intended location of your destination in one of these formats:')
                    try:
                        dest = input('C:\\\\Users\\\\Admin\\\\new_file.txt OR C:/Users/Admin/new_file.txt: ')

                        try: # Check for valid filepath
                            with open(dest) as file:
                                tmp = 1
                                del tmp
                        except FileNotFoundError:
                            print('Entry failed, please use the correct format!')
                            continue
                        break
                    except SyntaxError: # Used C:\ instead of C:\\ or C:/
                        print('Entry failed, please use the correct format!')
                        continue 
            elif dest_type == '3': # Print to command line
                break
            else:
                print('That is not an option, please try again.')
                continue
        for attempt in range(6): # 3 password attempts, arbitrary number used
            attempt += 1
            if attempt > 3:
                print("All attempts used, please start again.")
                del source, source_location, source_type, dest, dest_type, verify
                break
            print('\nPlease confirm your identity (attempt {} of 3): '.format(attempt+1))
            verify = accounts.user_entry()
            if verify['e_user'] == E_USER:
                print('Generating encryption key...')
                processing = Crypter(verify['pass'], source)
                processing.encryption_key = True

                print('Encrypting text...')
                write_text(processing.encrypter(), dest, False)
                print('Done! Check {} to see your encrypted file.'.format(dest))
                del source, source_location, source_type, dest, dest_type, verify, processing
                break
            else:
                print('That is not the correct password.')
        continue
    elif re.match('q', option.lower()): # quit
        break
    else:
        print('\nThat is not a valid option, please try again.')
        continue
del E_USER
print('\nThank you for using Textcryption!')