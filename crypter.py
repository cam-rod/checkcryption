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
      fragments = [] # Individual numbers in encryption key
      print("Generating encryption key...")
      for i in self.password[0:4]: # 1st-4th characters of the password
        if i == ('N' or 'r' or '(' or 'D' or 'c' or '.' or 'V'):
          fragments.append(0)
        elif i == ('Q' or 'n' or 'J' or 'e' or 'Z' or 'a' or 'k'):
          fragments.append(1)
        elif i == ('i' or '7' or '*' or 'z' or 'H' or 'u' or 'y'):
          fragments.append(2)
        elif i == ('S' or 'F' or '[' or 'j' or 'h' or 'R' or '3' or 'x'):
          fragments.append(3)
        elif i == ('p' or 'Y' or 'o' or '#' or '5' or 'w' or 'U'):
          fragments.append(4)
        elif i == ('b' or 'T' or '0' or 'g' or 'K' or 'A' or '2'):
          fragments.append(5)
        elif i == ('@' or 'X' or 'v' or 'I' or '8' or 's' or '1'):
          fragments.append(6)
        elif i == (')' or 'O' or 'd' or 'l' or 'L' or 'q' or 'C'):
          fragments.append(7)
        elif i == ('/' or ',' or 'W' or '4' or 't' or 'P' or 'B' or '9'):
          fragments.append(8)
        else:
          fragments.append(9)
      for i in self.password[4:8]: # 5th-8th characters of the password
        if i == ('A' or 'i' or 'y' or '5' or 'o' or 'X' or 't'):
          fragments.append(0)
        elif i == ('.' or 'c' or 'e' or 'D' or 'k' or 'U' or 'Q' or '1'):
          fragments.append(1)
        elif i == ('H' or 'v' or 'a' or 'N' or 'x' or 'J' or '@'):
          fragments.append(2)
        elif i == ('q' or 'B' or ']' or 'g' or '*' or 'L' or '6'):
          fragments.append(3)
        elif i == ('G' or 's' or '0' or 'Z' or 'O' or 'd' or 'b' or 'p'):
          fragments.append(4)
        elif i == ('l' or 'w' or ',' or '9' or '2' or 'n' or 'M'):
          fragments.append(5)
        elif i == ('E' or 'T' or 'f' or '/' or 'z' or '7' or '(' or 'I'):
          fragments.append(6)
        elif i == ('u' or 'C' or 'F' or 'S' or 'P' or 'Y' or 'h'):
          fragments.append(7)
        elif i == ('3' or 'R' or '#' or '!' or '8' or 'K' or 'm'):
          fragments.append(8)
        else:
          fragments.append(9)