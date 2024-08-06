import tkinter
from pandastable import Table
import matplotlib.pyplot as plt
from tkinter import *
import pandas
import sqlite3
import os

#building the main window
primary = tkinter.Tk()
primary.geometry('300x200')
primary.resizable(width=False,height=False)
primary.title("Computer Recon")

#Look into this https://www.daniweb.com/programming/software-development/threads/124403/sqlite3-how-to-see-column-names-for-table
def mpltest():
    fig, ax = plt.subplots()

    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')
    plt.show()



def aboutme():
     amWindow = tkinter.Toplevel()
     amWindow.geometry("200x200")
     tkinter.Label(amWindow,text=r"Made by AA-Ron Ogle. All this program does Is show a visual of data in a neat way.",wraplength=185,justify="center").pack()
     mpltest()




query = ("SELECT"
         " COUNT('OS Name')as OS,"
         " COUNT('OS Manufacturer') as Manufacturer"
         " FROM OperatingSystem")

#https://www.plus2net.com/python/tkinter-mysql.php
def create_new_pt():
    newpt = tkinter.Toplevel()
    #newpt.resizable(width=False,height=False)
    cnx = sqlite3.connect(database=os.path.join(os.pardir, 'data', "testdb.db"))
    df= pandas.read_sql(query, cnx)
    svb = tkinter.Frame(newpt)
    svb.pack(fill='both', expand=True)
    Table(svb,dataframe=df,showtoolbar=True,showstatusbar=True).show()
    if excelControlVar.get() == True:
        df.to_excel(tkinter.filedialog.asksaveasfilename(filetypes=[("SQLite Things","*.db")]))




#All teh buttons, and their placement in the grid as well as their commands.
about_me = (Button(primary,text="About",command=aboutme).grid(row=0,column=0))

summary = (Button(primary,text="Summary",command="").grid(row=1,column=0))

summary_visual = (Button(primary,text="Summary Visual",command=create_new_pt).grid(row=2,column=0))


#Control Variables for the CheckButton Widgets
csvControlVar = tkinter.IntVar()
excelControlVar = tkinter.IntVar()

#Checkbox for export to csv or excel

csv_checkbox = (Checkbutton(primary,text="CSV Export",command="",variable=csvControlVar,relief="sunken").grid(row=0,column=3))

excel_checkbox = (Checkbutton(primary,text="Excel Export",command="",variable=excelControlVar,relief="sunken").grid(row=1,column=3))



mainlable = (tkinter.Label(primary,text=f"Hello there...{os.getlogin()}?").place(relx=0.0,rely=1.0,anchor="sw"))





primary.mainloop()

