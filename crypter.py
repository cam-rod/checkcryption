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
  def encryption_key(self): # Stored as property to allow other areas to allow encryter decryptor to call key
    return self._encryption_key
  
  @encryption_key.setter
  def encryption_key(self, password):
    "This function generates the encryption key."
    if self.password != None:
      for i in self.password: # Each character of the password