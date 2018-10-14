"""This is the main module of Checkcryption.

This module introduces the program and calls other module to carry out specific actions."""

from crypterCore import accounts # Account creation or sign in
from crypterCore import menus # Program menus

print("Welcome to Checkcryption, the program that helps you verify your data!")

E_USER = accounts.main(True) # Signs in user

if E_USER is None: # User opted to quit
    pass
else:
    menus.main(E_USER)

print('\nThank you for using Checkcryption!')
