"""This module handles the encryption of decryption of data.

Arguments:
  - text: in the form of plaintext (to be encrypted) or encrypted data (to be decrypted), depending on what is requested
  - password: the user password which is converted into the encryption key

Other variables:
  - hashed_password: hashed (scrambled) version of the password, used to generate the encryption key
  - encryption_key: the key which directly instructs the program how to encrypt the data

Returns:
  - crypted_text: the encrypted (after encryption) or plaintext data (after decryption)
"""

