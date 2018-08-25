"""This module handles the encryption of decryption of data."""

import re

class Crypter:
    """This class generates the encryption key, calls the correct function, and returns the text.

    Arguments:
        - password: hashed (scrambled) version of the password, used to generate the encryption key
        - text: in plaintext (for encryption) or encrypted (for decryption) depending on the request

    Other variables:
        - encryption_key: directly instructs the program how to encrypt the data (hashed and salted)

    Returns:
        - the encrypted (after encryption) or plaintext data (after decryption)."""

    def __init__(self, password, text):
        """Initializes the variables."""
        self.password = password
        self.text = text
        self._encryption_key = None
    @property
    def encryption_key(self): # Stored as property to allow other areas to call key
        """Returns the encryption key."""
        return self._encryption_key
    @encryption_key.setter
    def encryption_key(self, value):
        """This function generates the encryption key."""
        if value:
            nums = [] # Individual numbers in encryption key
            salt = [] # Salted numbers to be added to e
            print("Generating encryption key...")
            for i in self.password[0:4]: # 1st-4th characters of the password
                if re.match(r'[Nr(Dc.V]', i):
                    nums.append(0)
                elif re.match(r'[QnJeZak]', i):
                    nums.append(1)
                elif re.match(r'[i7*zHuy]', i):
                    nums.append(2)
                elif re.match(r'[SF[jhR3x]', i):
                    nums.append(3)
                elif re.match(r'[pYo#5wU]', i):
                    nums.append(4)
                elif re.match(r'[bT0gKA2]', i):
                    nums.append(5)
                elif re.match(r'[@XvI8s1]', i):
                    nums.append(6)
                elif re.match(r'[)OdlLqC]', i):
                    nums.append(7)
                elif re.match(r'[/,W4tPB9]', i):
                    nums.append(8)
                else:
                    nums.append(9)
            for i in self.password[4:8]: # 5th-8th characters of the password
                if re.match(r'[Aiy5oXt]', i):
                    nums.append(0)
                elif re.match(r'[.ceDkUQ1]', i):
                    nums.append(1)
                elif re.match(r'[HvaNxJ@]', i):
                    nums.append(2)
                elif re.match(r'[qB\]g*L6]', i):
                    nums.append(3)
                elif re.match(r'[Gs0ZOdbp]', i):
                    nums.append(4)
                elif re.match(r'[lw,92nM]', i):
                    nums.append(5)
                elif re.match(r'[ETf/z7(I]', i):
                    nums.append(6)
                elif re.match(r'[uCFSPYh]', i):
                    nums.append(7)
                elif re.match(r'[3R#!8Km]', i):
                    nums.append(8)
                else:
                    nums.append(9)
            for i in self.password[8:12]: # 9th-12th characters of the password
                if re.match(r'[Fw9@#oS]', i):
                    nums.append(0)
                elif re.match(r'[P4hXqaJ]', i):
                    nums.append(1)
                elif re.match(r'[]CgHzBR]', i):
                    nums.append(2)
                elif re.match(r'[7,eQtLm]', i):
                    nums.append(3)
                elif re.match(r'[Dp1U83(]', i):
                    nums.append(4)
                elif re.match(r'[csfT.kZi]', i):
                    nums.append(5)
                elif re.match(r'[MYn5/vW]', i):
                    nums.append(6)
                elif re.match(r'[Ky!NGu0V]', i):
                    nums.append(7)
                elif re.match(r'[O[)IlbE]', i):
                    nums.append(8)
                else:
                    nums.append(9)

            # Begin salting, first quartet
            if (nums[3] - nums[1]) < (nums[2] + nums[0]):
                if nums[2] > nums[3]:
                    if (nums[0] + nums[1] + nums[2] + nums[3]) >= 12:
                        salt.append(0)
                    else:
                        salt.append(6)
                elif nums[1] == 4:
                    salt.append(7)
                else:
                    salt.append(1)
            elif ((nums[0] + nums[3]) % 2) == 0:
                salt.append(5)
            else:
                salt.append(8)
            # Begin salting, second quartet
            if (nums[7] % 3) == 0:
                if (nums[5] - nums[4]) > nums[6]:
                    salt.append(2)
                elif ((nums[7] * nums[5])+nums[6]) > (nums[6] * 4):
                    salt.append(4)
                elif (nums[4] + 5) > (nums[7] + 2):
                    salt.append(9)
                else:
                    salt.append(7)
            elif (nums[5] + 2) >= 7:
                if nums[4] < 8:
                    salt.append(3)
                else:
                    salt.append(0)
            else:
                salt.append(6)
            # Begin salting, third quartet
            if (nums[8] - nums[11] + nums[10]) > nums[9]:
                if (((nums[10] + nums[9]) or (nums[10] - nums[11])) % 2) == 0:
                    salt.append(7)
                elif nums[10] == (nums[8] or nums[9] or nums[11]):
                    salt.append(2)
                else:
                    salt.append(4)
            elif (nums[9] <= nums[11]) or (nums[10] <= nums[11]):
                if nums[10] == (2 or 5 or 7 or 8):
                    salt.append(1)
                elif nums[8] * 2 >= 9:
                    salt.append(5)
                else:
                    salt.append(3)
            else:
                if nums[8] < 6:
                    salt.append(9)
                else:
                    salt.append(8)
            # Begin salting, all numbers
            salt.append((nums[4] + (nums[7] + (nums[8] - nums[5]))
                             * nums[1] + ((nums[11] + nums[9] + nums[6]) - (nums[2] + nums[0]) * 5)
                             - nums[3] + nums[10]) % 10)

            # Salting the encryption key
            nums.insert(2, salt[0])
            nums.insert(9, salt[1])
            nums.insert(11, salt[2])
            nums.insert(7, salt[3])

            for i in enumerate(nums): # int to str converter
                nums[i[0]] = str(nums[i[1]])

            self._encryption_key = ''.join(nums) # The encryption key
            del nums
            del salt
            print('Encryption key generated!')
        else:
            pass # Request denied by program

    def encrypter(self):
        """This encrypts the text."""
        pass

    def decrypter(self):
        """This decrypts the text."""
        pass
