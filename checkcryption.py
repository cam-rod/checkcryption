"""This is the main module of Checkcryption.

This module introduces the program and calls other module to carry out specific actions."""

import tkinter as tk # GUI
from crypterCore import accounts # Account creation or sign in
from crypterCore import menus # Program menus

# Introduction

class Border(tk.Frame):
    """This class creates a popup for the program introduction and closing."""
    def __init__(self, text, master=None):
        """Generates the popup with inputted text."""
        super().__init__(master)
        
        # Config
        self.master.title('Checkcryption')
        self.master.iconbitmap(bitmap='checkcryption_logo.ico')
        self.master.maxsize(width=320, height=100)
        self.after(4000, root.destroy)

        # Text
        tk.Label(text=text, font='{none 47 none}', wraplength=300, width=31, justify='left',
                 anchor='w').grid(column=0, row=0)

root = tk.Tk()
welcome = Border('Welcome to Checkcryption, the program that helps you verify your data!',
                 master=root)
welcome.mainloop()

E_USER = accounts.main('setup') # Signs in user

if E_USER is None: # User opted to quit
    pass
else:
    menus.main(E_USER)

root = tk.Tk()
goodbye = Border('Thank you for using Checkcryption!', master=root)
goodbye.mainloop()
