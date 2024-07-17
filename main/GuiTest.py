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
    New_Window()

def change_text2():
    first_button.config(text=os.environ['HOMEPATH'])

#https://pythonguides.com/python-tkinter-multiple-windows-tutorial/
HEIGHT = 300
WIDTH = 500
def New_Window():
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window, height=HEIGHT, width=WIDTH)
    a_button = Button(Window, text="Don't click here?", command=change_text)
    a_button.place(x=150,y=25)
    canvas.pack()
    b_button = Button(Window, text="envion test", command=change_text2)
    print("New Window!")






first_button = Button(root,text ="Click Here",command=change_text2)
first_button.place(x=150,y=25)
print("Main Loop")
root.mainloop()
print("out of loop")
#Look at this: https://www.geeksforgeeks.org/how-to-place-a-button-at-any-position-in-tkinter/


#test file pathing

print(os.path.join(os.environ['HOMEPATH']))