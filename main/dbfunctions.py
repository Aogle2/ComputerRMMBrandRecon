"""

use this file to create the functions needed to interact with the Database.
This is going to use Pandas for the exporting of the DB into a csv or excel file.

"""
from pathlib import Path
import pandas as pd
from pandastable import Table, TableModel
import tkinter
import os




##Create one that is used over and over to check if the DB is present and to run a test if the file is valid.
def file_check(dbname):
    filepath = os.path.join(os.pardir,'data',dbname)
    if Path(filepath).is_file():
        print(f"{dbname} exist.")
    else:
        print(f"{dbname} does not exist or you or I mistyped the file")

file_check("TestDB.db")



#Create a function that will do the select test with one table at a tiem.




#Create a function that will do a select with diffrent joins.

#Create a function that will show the diffrent plots using matplotlib


#creat a function that will export it to a csv or excel file.