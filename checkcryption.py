"""This is the main module of Checkcryption.

This module introduces the program and calls other module to carry out specific actions."""

import tkinter as tk # GUI
from crypterCore import accounts # Account creation or sign in
from crypterCore import menus # Program menus

# Introduction
welcome = tk.Tk()
welcome.title('Checkcryption')
welcome.iconbitmap(bitmap='checkcryption_logo.ico')
welcome.maxsize(width=320, height=100)
tk.Label(welcome, text='Welcome to Checkcryption, the program that helps you verify your data!',
         font='{none 47 none}', wraplength=300, width=31, justify='left',
         anchor='w').grid(column=0, row=0)
welcome.after(4000, welcome.destroy)
welcome.mainloop()

E_USER = accounts.main('setup') # Signs in user

if E_USER is None: # User opted to quit
    pass
else:
    menus.main(E_USER)

print('\nThank you for using Checkcryption!')
