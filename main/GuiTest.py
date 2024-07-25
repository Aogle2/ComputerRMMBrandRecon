import os
import random
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from tkinter import *
import main
import platform as pl


#https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/
root = tk.Tk()
root.geometry('400x400')
root.resizable(False, False)
root.title('Test')

def check_os():
    if pl.system() == 'Darwin':
        rootpath = 'HOME'
        return rootpath
    else:
        rootpath = 'HOMEPATH'
        return rootpath

def change_text ():
    first_button.config(text="Change Text")
    root.geometry('400x400')
    New_Window()

def change_text2():
    first_button.config(text=os.environ[check_os()])
    third_button = Button(root,text="I popped up",command=tkinter.filedialog.asksaveasfilename(filetypes=[("SQLite Things","*.db")])).grid(row=4, column=0)
    New_Window()
    root.geometry('800x600') #this is really cool


#https://pythonguides.com/python-tkinter-multiple-windows-tutorial/
HEIGHT = 300
WIDTH = 500
def New_Window():
    Window = tk.Toplevel()
    Window.geometry('320x250')
    canvas = tk.Canvas(Window, height=HEIGHT, width=WIDTH)
    first_button= Button(Window, text="Don't click here?", command=change_text).grid(row=1, column=0)
    Button(Window, text="envion test", command=change_text2)
    print("New Window!")






first_button = Button(root,text ="Click Here",command=change_text2)
buttonthin = Button(root,text="This thing",command=change_text).grid(row=24,column=5)
first_button.grid(row=5,column=6)
print("Main Loop")
root.mainloop()
print("out of loop")
#Look at this: https://www.geeksforgeeks.org/how-to-place-a-button-at-any-position-in-tkinter/


#Linux and Mac seem to use 'home' instead of 'homepath'

