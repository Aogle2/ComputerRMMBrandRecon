import tkinter
import matplotlib.pyplot as plt
from tkinter import *
import pandas
import sqlite3
import os

#building the main window this will be the main hub for how things are viewed.
#This is also the first thing that opens.
#Scaling will screw this up on diffrent platforms.
primary = tkinter.Tk()
primary.geometry('225x175')
primary.resizable(width=False,height=False)
primary.title("Computer Recon")

#This is the base query that pulls info from the DB, ths is system agnostic, tested to work on MacOS, Linux and Windows.
def basequery(query):
    cnx = sqlite3.connect(os.path.join(os.pardir, 'data', "TestDB.db"))
    df = pandas.read_sql(query, cnx)
    cnx.close()
    return df

#This is what gives the button their functionality, this runs the base query
def venderview():
    query = basequery("SELECT vtype as [Vendor Type], COUNT(vName) as Count FROM Vendor GROUP BY vtype ORDER BY COUNT(vName);")
    query['Vendor Type'] = query['Vendor Type'].astype(str)                 #set this as a string, ploting threw and error on data type. This is the only row affected.
    fig, ax = plt.subplots()
    bars = ax.bar(query['Vendor Type'], query['Count'])                     #This allows the bars generated to have annotation, selecting two columns.
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',xy=(bar.get_x() + bar.get_width() /2,height), xytext=(0,2),textcoords='offset points',ha='center',va='bottom')
    plt.xlabel('Vendor Type')
    plt.ylabel('Count')
    plt.title('What are the most common vendors are present? ')
    plt.tight_layout()                                                      #Adjust layout to prevent clipping of labels
    plt.show()                                                              #Show the plot


def osview():
    query = basequery("SELECT [OS Manufacturer], COUNT([OS Name]) AS Count FROM OperatingSystem GROUP BY [OS Manufacturer] ORDER BY COUNT([OS Name]);")
    query.fillna('Linux', inplace=True)  #These values were found to be linux..not a lot..but enough to break operation
    query['OS Manufacturer'] = query['OS Manufacturer'].astype(str)
    fig,ax = plt.subplots()
    bars = ax.bar(query['OS Manufacturer'], query['Count'])
    for bar in bars: #This is adding the annotation for the vertical bars, this adds the found value on the top.
        height = bar.get_height()
        ax.annotate(f'{height}',xy=(bar.get_x() + bar.get_width() /2,height), xytext=(0,2),textcoords='offset points',ha='center',va='bottom')
    plt.xlabel('Operating System')
    plt.ylabel('Count')
    plt.title('Count of Operating Systems Used in Enviroment')
    plt.tight_layout()
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
    plt.title('How many devices are using what Manufacturer?')
    plt.tight_layout()
    plt.show()

def aboutme():
     amWindow = tkinter.Toplevel()                                          #Make this window a child of the main window process, closes with the main Window.
     amWindow.geometry("200x200")
     tkinter.Label(amWindow,text=r"Made by AA-Ron Ogle. All this program does Is show a visual of data in a neat way.",wraplength=185,justify="center").pack()


#All teh buttons, and their placement in the grid as well as their commands.
(Button(primary,text="About",command=aboutme).pack())
(Button(primary,text="Vendor Summary",command=venderview).pack())
(Button(primary,text="Manufacturer Summary",command=manufacturersummary).pack())
(Button(primary,text="Operating System View",command=osview).pack())

(tkinter.Label(primary,text=f"Hello there...{os.getlogin()}?").place(relx=0.0,rely=1.0,anchor="sw"))

#Keep the main loop going, this does not close until you close the main window.
primary.mainloop()

