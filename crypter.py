"""This module handles the encryption of decryption of data."""

import re

class Crypter:
  """This class temporarily generates the encryption key, calls the correct function, and then returns the text.

  Arguments:
    - password: hashed (scrambled) version of the password, used to generate the encryption key
    - text: in the form of plaintext (to be encrypted) or encrypted data (to be decrypted), depending on what is requested

  Other variables:
    - encryption_key: the key which directly instructs the program how to encrypt the data (hashed and salted)

  Returns:
    - the encrypted (after encryption) or plaintext data (after decryption)."""

  def __init__(self, password, text):
    """Initializes the variables."""
    self.password = password
    self.text = text
  
  @property
  def encryption_key(self): # Stored as property to allow other areas to allow encrypter/decrypter to call key
    return self._encryption_key
  
  @encryption_key.setter
  def encryption_key(self, value):
    "This function generates the encryption key."
    if value:
      e = [] # Individual numbers in encryption key
      salt = [] # Salted numbers to be added to e
      print("Generating encryption key...")
      for i in self.password[0:4]: # 1st-4th characters of the password
        if re.match(r'[Nr\(Dc\.V]', i) != None:
          e.append(0)
        elif re.match(r'[QnJeZak]', i) != None:
          e.append(1)
        elif re.match(r'[i7\*zHuy]', i) != None:
          e.append(2)
        elif re.match(r'[SF\[jhR3x]', i) != None:
          e.append(3)
        elif re.match(r'[pYo#5wU]', i) != None:
          e.append(4)
        elif re.match(r'[bT0gKA2]', i) != None:
          e.append(5)
        elif re.match(r'[@XvI8s1]', i) != None:
          e.append(6)
        elif re.match(r'[\)OdlLqC]', i) != None:
          e.append(7)
        elif re.match(r'[/,W4tPB9]', i) != None:
          e.append(8)
        else:
          e.append(9)
      for i in self.password[4:8]: # 5th-8th characters of the password
        if re.match(r'[Aiy5oXt]', i) != None:
          e.append(0)
        elif re.match(r'[\.ceDkUQ1]', i) != None:
          e.append(1)
        elif re.match(r'[HvaNxJ@]', i) != None:
          e.append(2)
        elif re.match(r'[qB\]g\*L6]', i) != None:
          e.append(3)
        elif re.match(r'[Gs0ZOdbp]', i) != None:
          e.append(4)
        elif re.match(r'[lw,92nM]', i) != None:
          e.append(5)
        elif re.match(r'[ETf/z7\(I]', i) != None:
          e.append(6)
        elif re.match(r'[uCFSPYh]', i) != None:
          e.append(7)
        elif re.match(r'[3R#!8Km]', i) != None:
          e.append(8)
        else:
          e.append(9)
      for i in self.password[8:12]: # 9th-12th characters of the password
        if re.match(r'[Fw9@#oS]', i) != None:
          e.append(0)
        elif re.match(r'[P4hXqaJ]', i) != None:
          e.append(1)
        elif re.match(r'[\]CgHzBR]', i) != None:
          e.append(2)
        elif re.match(r'[7,eQtLm]', i) != None:
          e.append(3)
        elif re.match(r'[Dp1U83\(]', i) != None:
          e.append(4)
        elif re.match(r'[csfT\.kZi]', i) != None:
          e.append(5)
        elif re.match(r'[MYn5/vW]', i) != None:
          e.append(6)
        elif re.match(r'[Ky!NGu0V]', i) != None:
          e.append(7)
        elif re.match(r'[O\[\)IlbE]', i) != None:
          e.append(8)
        else:
          e.append(9)

      # Begin salting, first quartet
      if (e[3] - e[1]) < (e[2] + e[0]):
        if e[2] > e[3]:
          if (e[0] + e[1] + e[2] + e[3]) >= 12:
            salt.append(0)
          else:
            salt.append(6)
        elif e[1] == 4:
          salt.append(7)
        else:
          salt.append(1)
      elif ((e[0] + e[3]) % 2) == 0:
        salt.append(5)
      else:
        salt.append(8)
      
      # Begin salting, second quartet
      if (e[7] % 3) == 0:
        if (e[5] - e[4]) > e[6]:
          salt.append(2)
        elif ((e[7] * e[5])+e[6]) > (e[6] * 4):
          salt.append(4)
        elif (e[4] + 5) > (e[7] + 2):
          salt.append(9)
        else:
          salt.append(7)
      elif (e[5] + 2) >= 7:
        if e[4] < 8:
          salt.append(3)
        else:
          salt.append(0)
      else:
        salt.append(6)
      
      # Begin salting, third quartet
      if (e[8] - e[11] + e[10]) > e[9]:
        if (((e[10] + e[9]) or (e[10] - e[11])) % 2) == 0:
          salt.append(7)
        elif e[10] == (e[8] or e[9] or e[11]):
          salt.append(2)
        else:
          salt.append(4)
      elif (e[9] <= e[11]) or (e[10] <= e[11]):
        if e[10] == (2 or 5 or 7 or 8):
          salt.append(1)
        elif e[8] * 2 >= 9:
          salt.append(5)
        else:
          salt.append(3)
      else:
        if e[8] < 6:
          salt.append(9)
        else:
          salt.append(8)
      
      # Begin salting, all numbers
      salt.append(str((e[4] + (e[7] + (e[8] - e[5])) * e[1] + ((e[11] + e[9] + e[6]) - (e[2] + e[0]) * 5) - e[3] + e[10]) % 10))

      # Salting the encryption key
      e.insert(2,salt[0])
      e.insert(9,salt[1])
      e.insert(11,salt[2])
      e.insert(7,salt[3])

      for i in range(len(e)): # int to str converter
        e[i] = str(e[i])

      self._encryption_key = ''.join(e) # The encryption key
      del e
      del salt
      del password
    else:
      pass # Request denied by program

  def encrypter(self):
    """This encrypts the text."""
    pass

  def decrypter(self):
    """This decrypts the text."""
    pass