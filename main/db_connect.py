import os
import sqlite3
import sqlite3 as sql
from pathlib import Path

import pandas


#This checks to see if the db file is present. This is for now, almost a hardcoded path.
def file_check(dbname):
    filepath = os.path.join(os.pardir,'data',dbname)
    if Path(filepath).is_file():
        print(f"{dbname} exist.")
    else:
        print(f"{dbname} does not exist or you or I mistyped the file")



#Overview here: https://realpython.com/primer-on-python-decorators/




#--------------------------------------------------
def db_test():
    results = []
    DB = sql.connect(database= os.path.join(os.pardir,'data',"TestDB.db"))
    cur = DB.cursor()
    cur.execute('SELECT * FROM OperatingSystem;')#cur.execute('SELECT sqlite_version()')
    for row in cur.fetchall(): #results = cur.fetchone()[-1]
          row += results
    if results:
        print("data is present.")
    return results

def pd_sql():
    cnx = sqlite3.connect(database=os.path.join(os.pardir,'data',"testdb.db"))
    df = pandas.read_sql("SELECT * FROM Vendor",cnx)
    return df.to_string()


#look into this https://stackoverflow.com/questions/71362727/python-sqlite3-insert-data-from-for-loop
