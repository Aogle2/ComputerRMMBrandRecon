import tkinter
from pandastable import Table
import matplotlib.pyplot as plt
from tkinter import *
import pandas
import sqlite3
import os

#building the main window
primary = tkinter.Tk()
primary.geometry('325x350')
primary.resizable(width=False,height=False)
primary.title("Computer Recon")

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

#Consolidate how I want the data to be retreaved, saves time instead of typing this over and over.
def basequery(query):
    cnx = sqlite3.connect(database=os.path.join(os.pardir, 'data', "TestDB.db"))
    df = pandas.read_sql(query, cnx)
    cnx.close()
    return df

#for creating the value numbers on the bars
#https://www.geeksforgeeks.org/adding-value-labels-on-a-matplotlib-bar-chart/

def venderview():
    query = basequery("SELECT vtype as [Vendor Type], COUNT(vName) as Count FROM Vendor GROUP BY vtype;")
    query['Vendor Type'] = query['Vendor Type'].astype(str)
    #Split the df into two list

    plt.bar(query['Vendor Type'], query['Count'])
    plt.xlabel('Vendor Type')
    plt.ylabel('Count')
    plt.title('Count of Vendors Used')  # Rotate x-axis labels if needed
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()


def osview():
    query = basequery("SELECT [OS Manufacturer], COUNT([OS Name]) AS Count FROM OperatingSystem GROUP BY [OS Manufacturer];")
    query.fillna('Linux', inplace=True)
    query['OS Manufacturer'] = query['OS Manufacturer'].astype(str)
    #Split the query into two list

    plt.bar(query['OS Manufacturer'], query['Count'])
    plt.xlabel('Operating System')
    plt.ylabel('Count')
    plt.title('Count of Operating Systems')  # Rotate x-axis labels if needed
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def manufacturersummary():
    query = basequery("SELECT vName as [Vendor Name], COUNT(vtype) as Count FROM Model JOIN Vendor ON Model.v_id = Vendor.v_id GROUP BY vType ORDER BY (COUNT(vName)) LIMIT 5")
    query['Vendor Name'] = query['Vendor Name'].astype(str)
    #Split the query into two list.

    plt.bar(query['Vendor Name'], query['Count'])
    plt.xlabel('Vendor Name')
    plt.ylabel('Count')
    plt.title('Count of Vendors Used')  # Rotate x-axis labels if needed
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def aboutme():
     amWindow = tkinter.Toplevel()
     amWindow.geometry("200x200")
     tkinter.Label(amWindow,text=r"Made by AA-Ron Ogle. All this program does Is show a visual of data in a neat way.",wraplength=185,justify="center").pack()




#All teh buttons, and their placement in the grid as well as their commands.
(Button(primary,text="About",command=aboutme).grid(row=0,column=0))
(Button(primary,text="Vendor Summary",command=venderview).grid(row=1,column=0))
(Button(primary,text="Manufacturer Summary",command=manufacturersummary).grid(row=2,column=0))
(Button(primary,text="Operating System View",command=osview).grid(row=3,column=0))

(tkinter.Label(primary,text=f"Hello there...{os.getlogin()}?").place(relx=0.0,rely=1.0,anchor="sw"))





primary.mainloop()

