import os
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.geometry('300x320')
root.resizable(False, False)
root.title('Test')

def change_text ():
    first_button.config(text="Change Text")


first_button = Button(root, text = "Click Here", command=change_text)
first_button.place(x=150,y=25)

root.mainloop()

#Look at this: https://www.geeksforgeeks.org/how-to-place-a-button-at-any-position-in-tkinter/
