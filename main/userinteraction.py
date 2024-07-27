import tkinter
from tkinter import *
import os
import pandastable as pt


#building the main window
root = tkinter.Tk()
root.geometry('300x300')
root.resizable(width=False,height=False)
root.title("Computer Recon")


#All teh buttons, and their placement in the grid as well as their commands.
Button(root,text="About",command="").grid(row=0,column=0)
Button(root, text="Summary",command="").grid(row=1,column=0)
Button(root,text="Summary Visual",command="").grid(row=2,column=0)


#Control Variables for the CheckButton Widgets
csvControlVar = tkinter.IntVar()
excelControlVar = tkinter.IntVar()

#Checkbox for export to csv or excel
def check_CSV_export():
    print(csvControlVar.get())

def check_Excel_export():
    print(excelControlVar.get())

Checkbutton(root,text="CSV Export",command=check_CSV_export,variable=csvControlVar).grid(row=0,column=3)
Checkbutton(root,text="Excel Export",command=check_Excel_export,variable=excelControlVar).grid(row=1,column=3)









root.mainloop()

