import tkinter
from tkinter import *

import os
from time import sleep
#import pandastable as pt


#building the main window
primary = tkinter.Tk()
primary.geometry('300x200')
primary.resizable(width=False,height=False)
primary.title("Computer Recon")




def aboutme():
     amWindow = tkinter.Toplevel()
     amWindow.geometry("200x200")
     tkinter.Label(amWindow,
                   text=r"Made by AA-Ron Ogle. All this program does Is show a visual of data in a neat way.",
                   wraplength=185,
                   justify="center").pack()






#All teh buttons, and their placement in the grid as well as their commands.
about_me = (Button(primary,
       text="About",
       command=aboutme)
        .grid(row=0,column=0))

summary = (Button(primary,
       text="Summary",
       command="")
            .grid(row=1,column=0))

summary_visual = (Button(primary,
       text="Summary Visual",
       command="")
            .grid(row=2,column=0))


#Control Variables for the CheckButton Widgets
csvControlVar = tkinter.IntVar()
excelControlVar = tkinter.IntVar()

#Checkbox for export to csv or excel
def check_CSV_export():
    print(csvControlVar.get())

def check_Excel_export():
    print(excelControlVar.get())

csv_checkbox = (Checkbutton(primary,
            text="CSV Export",
            command=check_CSV_export,
            variable=csvControlVar,
            relief="sunken")
                .grid(row=0,column=3))

excel_checkbox = (Checkbutton(primary,
            text="Excel Export",
            command=check_Excel_export,
            variable=excelControlVar,
            relief="sunken")
                .grid(row=1,column=3))



mainlable = (tkinter.Label(primary,
                          text=f"Hello there...{os.getlogin()}?")
                                .place(relx=0.0,rely=1.0,anchor="sw"))





primary.mainloop()

