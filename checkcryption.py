"""This is the main module of Checkcryption.

This module introduces the program and calls other module to carry out specific actions."""

import tkinter as tk # GUI
from crypterCore import accounts # Account creation or sign in
from crypterCore import menus # Program menus

# GUI basic frame

class Outline(tk.Frame):
    """This class provides the base details for all windows in Checkcryption."""
    def __init__(self, master, width, height):
        """This generates the title, logo, and sizing for GUI elements.
        
        master: initializes tkinter
        width/height: dimensions of the window"""
        super().__init__(master)

        # Center popup prep
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # Basic Config
        self.master.title('Checkcryption')
        self.master.iconbitmap(bitmap='checkcryption_logo.ico')
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Introduction

class Border(Outline):
    """This class creates a popup for the program introduction and closing."""
    def __init__(self, text, master, width, height, init):
        """Generates the popup with inputted text."""
        super().__init__(master, width, height)
        
        # Config
        self.after(4000, root.destroy)
        tk.Label(text=text, font='{none 47 none}', wraplength=300, width=31, justify='left',
                 anchor='w').grid(column=0, row=0)
        if init: # Opening program
            tk.Label(text='Logo attribution: LOCK check mark by Tony Wallström from' +
                     'thenounproject.com', font='{none 47 none}', wraplength=300, width=31,
                     justify='left', anchor='w').grid(column=0, row=1, ipady=16)

root = tk.Tk()
welcome = Border('Welcome to Checkcryption, the program that helps you verify your data!', root,
                 285, 100, True)
welcome.mainloop()

E_USER = accounts.main('setup') # Signs in user

if E_USER is None: # User opted to quit
    pass
else:
    menus.main(E_USER)

root = tk.Tk()
goodbye = Border('Thank you for using Checkcryption!', root, 245, 25, False)
goodbye.mainloop()
