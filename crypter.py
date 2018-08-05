"""This module handles the encryption of decryption of data."""

class Crypter:
  """This class temporarily generates the encryption key, calls the correct function, and then returns the text.

  Arguments:
    - password: hashed (scrambled) version of the password, used to generate the encryption key
    - text: in the form of plaintext (to be encrypted) or encrypted data (to be decrypted), depending on what is requested
    - crypt: what should happen to the text (encryption or decryption)

  Other variables:
    - encryption_key: the key which directly instructs the program how to encrypt the data (hashed and salted)

  Returns:
    - the encrypted (after encryption) or plaintext data (after decryption)
  """

  def __init__(self, password, text, crypt):
    """Initializes the variables."""
    self.password = password
    self.text = text
    self.crypt = crypt
  
  @property
  def encryption_key(self): # Stored as property to allow other areas to allow encrypter/decrypter to call key
    return self._encryption_key
  
  @encryption_key.setter
  def encryption_key(self, password):
    "This function generates the encryption key."
    if self.password != None:
      e = [] # Individual numbers in encryption key
      salt = [] # Salted numbers to be added to e
      print("Generating encryption key...")
      for i in self.password[0:4]: # 1st-4th characters of the password
        if i == ('N' or 'r' or '(' or 'D' or 'c' or '.' or 'V'):
          e.append(0)
        elif i == ('Q' or 'n' or 'J' or 'e' or 'Z' or 'a' or 'k'):
          e.append(1)
        elif i == ('i' or '7' or '*' or 'z' or 'H' or 'u' or 'y'):
          e.append(2)
        elif i == ('S' or 'F' or '[' or 'j' or 'h' or 'R' or '3' or 'x'):
          e.append(3)
        elif i == ('p' or 'Y' or 'o' or '#' or '5' or 'w' or 'U'):
          e.append(4)
        elif i == ('b' or 'T' or '0' or 'g' or 'K' or 'A' or '2'):
          e.append(5)
        elif i == ('@' or 'X' or 'v' or 'I' or '8' or 's' or '1'):
          e.append(6)
        elif i == (')' or 'O' or 'd' or 'l' or 'L' or 'q' or 'C'):
          e.append(7)
        elif i == ('/' or ',' or 'W' or '4' or 't' or 'P' or 'B' or '9'):
          e.append(8)
        else:
          e.append(9)
      for i in self.password[4:8]: # 5th-8th characters of the password
        if i == ('A' or 'i' or 'y' or '5' or 'o' or 'X' or 't'):
          e.append(0)
        elif i == ('.' or 'c' or 'e' or 'D' or 'k' or 'U' or 'Q' or '1'):
          e.append(1)
        elif i == ('H' or 'v' or 'a' or 'N' or 'x' or 'J' or '@'):
          e.append(2)
        elif i == ('q' or 'B' or ']' or 'g' or '*' or 'L' or '6'):
          e.append(3)
        elif i == ('G' or 's' or '0' or 'Z' or 'O' or 'd' or 'b' or 'p'):
          e.append(4)
        elif i == ('l' or 'w' or ',' or '9' or '2' or 'n' or 'M'):
          e.append(5)
        elif i == ('E' or 'T' or 'f' or '/' or 'z' or '7' or '(' or 'I'):
          e.append(6)
        elif i == ('u' or 'C' or 'F' or 'S' or 'P' or 'Y' or 'h'):
          e.append(7)
        elif i == ('3' or 'R' or '#' or '!' or '8' or 'K' or 'm'):
          e.append(8)
        else:
          e.append(9)
      for i in self.password[8:12]: # 9th-12th characters of the password
        if i == ('F' or 'w' or '9' or '@' or '#' or 'o' or 'S'):
          e.append(0)
        elif i == ('P' or '4' or 'h' or 'X' or 'q' or 'a' or 'J'):
          e.append(1)
        elif i == (']' or 'C' or 'g' or 'H' or 'z' or 'B' or 'R'):
          e.append(2)
        elif i == ('7' or ',' or 'e' or 'Q' or 't' or 'L' or 'm'):
          e.append(3)
        elif i == ('D' or 'p' or '1' or 'U' or '8' or '3' or '('):
          e.append(4)
        elif i == ('c' or 's' or 'f' or 'T' or '.' or 'k' or 'Z' or 'i'):
          e.append(5)
        elif i == ('M' or 'Y' or 'n' or '5' or '/' or 'v' or 'W'):
          e.append(6)
        elif i == ('K' or 'y' or '!' or 'N' or 'G' or 'u' or '0' or 'V'):
          e.append(7)
        elif i == ('O' or '[' or ')' or 'I' or 'l' or 'b' or 'E'):
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
      salt.append(((e[4] + (e[7] + (e[8] - e[5])) * e[1] + ((e[11] + e[9] + e[6]) - (e[2] + e[0]) * 5) - e[3] + e[10]) % 10))