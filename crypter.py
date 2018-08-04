"""This module handles the encryption of decryption of data."""

def crypter(password, text, crypt):
  """This function temporarily generates the encryption key, calls the correct function, and then returns the text.

  Arguments:
    - password: hashed (scrambled) version of the password, used to generate the encryption key
    - text: in the form of plaintext (to be encrypted) or encrypted data (to be decrypted), depending on what is requested
    - crypt: what should happen to the text (encryption or decryption)

  Other variables:
    - encryption_key: the key which directly instructs the program how to encrypt the data

  Returns:
    - the encrypted (after encryption) or plaintext data (after decryption)
  """
  
    