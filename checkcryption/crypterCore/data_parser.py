"""This module interprets text from various sources.

Functions:
    - Gets and verifies a valid password for signing in.
    - Reads text from regular files or direct entry and returns it.
    - Converts text to binary.
    - Writes encrypted text to files.
    - Reads and returns matching section from users.txt.
    - Writes usernames to users.txt."""

import re
from checkcryption.checkcryption import Outline

class SignIn(Outline):
    """This class requests and returns the username and password to be used."""
    def __init__(self, master, width, height, choice='Sign in or create'):
        """This generates the outline and starts the windows of account handling."""
        super().__init__(master, width, height)
        self.windows(choice, master)

    def windows(self, choice, master):
        """This generates the GUI and returns the username and password."""
        tk = self.tk
        # Description
        tk.Label(text='{} your Checkcryption account.\n\nPassword requirements:'.format(choice) +
                 '\n  - Valid character are numbers, letters, and symbols ()[]!@#,.*/' +
                 '\n  - The password must be EXACTLY 12 characters long' +
                 '\n  - The password must include at least one lowercase letter, one uppercase ' +
                 'letter one number, and one symbol', justify='left',
                 anchor='w', font='{Arial 20}', wraplength=500).grid(column=0, row=0)
        
        # Text box labels
        username = tk.Label(text='Username:', font='{Consolas 20}', justify='left', anchor='w'
                            ).grid(column=0, row=1)
        password = tk.Label(text='Password:', font='{Consolas 20}', justify='left', anchor='w'
                            ).grid(column=0, row=2)

        # Input boxes
        tk.Entry(width=40, bg='#C0C2C3').grid(column=1, row=1, sticky='w')
        tk.Entry(width=40, show='•', bg='#C0C2C3').grid(column=1, row=2, sticky='w')

        # Buttons
        tk.Button(text='Submit', justify='center', anchor='center', width=6,
                  command=self.interpret(username, password, master)
                  ).grid(column=0, row=3)
        tk.Button(text='Quit Program', justify='center', anchor='center', width=12,
                  command=master.destroy).grid(column=0, row=3)

        return None
    
    def interpret(self, username, password, master):
        """This function interprets the pressed button and verifies the password validity."""
        userpass = [] # Returns username and password if valid
        reason = 'This is not a valid password.\n\n' # Reason for error message

        # Verify password
        if len(password) == 12:
            if re.search(r'^[A-Za-z\d()[\]!@#,.*/]*$', password): # only valid characters used
                if (re.search(r'[A-Z]', password)
                        and re.search(r'[a-z]', password)
                        and re.search(r'[0-9]', password)
                        and re.search(r'[()[\]!@#,.*/]', password)):
                    userpass = {'user': username, 'pass': password}
                    reason = None
                else:
                    reason += 'Reason: password did not meet minimum requirements.'
            else:
                reason += 'Reason: invalid characters used in password.'
        else:
            reason += 'Reason: password was not 12 characters long.'
        
        # Genereate window or quit
        if reason is None:
            master.destroy()
            return userpass
        else:
            error = self.tk.Toplevel()
            error.Label(text=reason).grid(column=0, row=0)
            error.after(3700, self.destroy)
            
            error.mainloop()

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
