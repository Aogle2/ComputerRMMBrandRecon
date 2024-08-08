import tkinter
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

#Consolidate how I want the data to be retreaved, saves time instead of typing this over and over.
def basequery(query):
    cnx = sqlite3.connect(database=os.path.join(os.pardir, 'data', "TestDB.db"))
    df = pandas.read_sql(query, cnx)
    cnx.close()
    return df

#for creating the value numbers on the bars
#https://www.geeksforgeeks.org/adding-value-labels-on-a-matplotlib-bar-chart/

def venderview():
    query = basequery("SELECT vtype as [Vendor Type], COUNT(vName) as Count FROM Vendor GROUP BY vtype ORDER BY COUNT(vName);")
    query['Vendor Type'] = query['Vendor Type'].astype(str)
    fig, ax = plt.subplots()
    bars = ax.bar(query['Vendor Type'], query['Count'])
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',xy=(bar.get_x() + bar.get_width() /2,height), xytext=(0,2),textcoords='offset points',ha='center',va='bottom')
    plt.xlabel('Vendor Type')
    plt.ylabel('Count')
    plt.title('What are the most common vendors are present? ')
    plt.tight_layout()
    plt.show()


def osview():
    query = basequery("SELECT [OS Manufacturer], COUNT([OS Name]) AS Count FROM OperatingSystem GROUP BY [OS Manufacturer] ORDER BY COUNT([OS Name]);")
    query.fillna('Linux', inplace=True)
    query['OS Manufacturer'] = query['OS Manufacturer'].astype(str)
    fig,ax = plt.subplots()
    bars = ax.bar(query['OS Manufacturer'], query['Count'])
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',xy=(bar.get_x() + bar.get_width() /2,height), xytext=(0,2),textcoords='offset points',ha='center',va='bottom')
    plt.xlabel('Operating System')
    plt.ylabel('Count')
    plt.title('Count of Operating Systems Used in Enviroment')  # Rotate x-axis labels if needed
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def manufacturersummary():
    query = basequery("SELECT vName as [Vendor Name], COUNT(vtype) as Count FROM Model JOIN Vendor ON Model.v_id = Vendor.v_id GROUP BY vType ORDER BY (COUNT(vName)) LIMIT 5")
    query['Vendor Name'] = query['Vendor Name'].astype(str)
    fig, ax = plt.subplots()
    bars = ax.bar(query['Vendor Name'], query['Count'])
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',xy=(bar.get_x() + bar.get_width() /2,height), xytext=(0,2),textcoords='offset points',ha='center',va='bottom')
    plt.xlabel('Vendor Name')
    plt.ylabel('Count')
    plt.title('How many devices are using what Manufacturer?')  # Rotate x-axis labels if needed
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

