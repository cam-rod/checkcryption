"""This is the main module of Textcryption.

This module introduces the program and calls other module to carry out specific actions."""

from crypterCore import accounts # Account creation or sign in
from crypterCore import menus # Program menus

print("Welcome to Textcryption, the program that helps you protect your data!")

E_USER = accounts.main() # Signs in user

if E_USER is None: # User opted to quit
    pass
else:
    menus.main(E_USER)

print('\nThank you for using Textcryption!')
