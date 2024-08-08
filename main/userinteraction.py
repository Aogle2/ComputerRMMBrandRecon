import tkinter
import matplotlib.pyplot as plt
from tkinter import *
import pandas
import sqlite3
import os

#building the main window
primary = tkinter.Tk()
primary.geometry('325x200')
primary.resizable(width=False,height=False)
primary.title("Computer Recon")

#Consolidate how I want the data to be retreaved, saves time instead of typing this over and over.
def basequery(query):
    cnx = sqlite3.connect(database=os.path.join(os.pardir, 'data', "TestDB.db"))
    df = pandas.read_sql(query, cnx)
    cnx.close()
    return df

#for creating the value numbers on the bars
#https://www.geeksforgeeks.org/adding-value-labels-on-a-matplotlib-bar-chart/

def osview():
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




#All teh buttons, and their placement in the grid as well as their commands.
(Button(primary,text="About",command=aboutme).grid(row=0,column=0))

(Button(primary,text="Summary",command="").grid(row=1,column=0))

(Button(primary,text="Operating System View",command=osview).grid(row=2,column=0))

(tkinter.Label(primary,text=f"Hello there...{os.getlogin()}?").place(relx=0.0,rely=1.0,anchor="sw"))





primary.mainloop()

