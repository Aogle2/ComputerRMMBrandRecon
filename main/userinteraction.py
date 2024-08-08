import tkinter
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

#Consolidate how I want the data to be retreaved, saves time instead of typing this over and over.
def basequery(query):
    cnx = sqlite3.connect(database=os.path.join(os.pardir, 'data', "TestDB.db"))
    df = pandas.read_sql(query, cnx)
    cnx.close()
    return df

#Look into this https://www.daniweb.com/programming/software-development/threads/124403/sqlite3-how-to-see-column-names-for-table

def newplot():
    testdf = basequery("SELECT [OS Manufacturer], COUNT([OS Name]) AS count FROM OperatingSystem GROUP BY [OS Manufacturer];")
    testdf.fillna('Linux', inplace=True)
    testdf['OS Manufacturer'] = testdf['OS Manufacturer'].astype(str)

    plt.bar(testdf['OS Manufacturer'], testdf['count'])
    plt.xlabel('Operating System')
    plt.ylabel('Count')
    plt.title('Count of Operating Systems')  # Rotate x-axis labels if needed
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def aboutme():
     amWindow = tkinter.Toplevel()
     amWindow.geometry("200x200")
     tkinter.Label(amWindow,text=r"Made by AA-Ron Ogle. All this program does Is show a visual of data in a neat way.",wraplength=185,justify="center").pack()





#query = ("SELECT"
#         " COUNT('OS Name')as OS,"
#         " COUNT('OS Manufacturer') as Manufacturer"
#         " FROM OperatingSystem")

query = ("SELECT COUNT(*) FROM OperatingSystem GROUP BY [OS Manufacturer]")

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

summary_visual = (Button(primary,text="Summary Visual",command=newplot).grid(row=2,column=0))


#Control Variables for the CheckButton Widgets
csvControlVar = tkinter.IntVar()
excelControlVar = tkinter.IntVar()

#Checkbox for export to csv or excel

#csv_checkbox = (Checkbutton(primary,text="CSV Export",command="",variable=csvControlVar,relief="sunken").grid(row=0,column=3))

#excel_checkbox = (Checkbutton(primary,text="Excel Export",command="",variable=excelControlVar,relief="sunken").grid(row=1,column=3))



mainlable = (tkinter.Label(primary,text=f"Hello there...{os.getlogin()}?").place(relx=0.0,rely=1.0,anchor="sw"))





primary.mainloop()

