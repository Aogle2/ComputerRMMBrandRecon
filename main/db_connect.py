import os
import sqlite3 as sql
from pathlib import Path


#This checks to see if the db file is present. This is for now, almost a hardcoded path.
def file_check(dbname):
    filepath = os.path.join(os.pardir,'data',dbname)
    if Path(filepath).is_file():
        print(f"{dbname} exist.")
    else:
        print(f"{dbname} does not exist or you or I mistyped the file")



file_check("TestDB.db")

#Overview here: https://realpython.com/primer-on-python-decorators/




#--------------------------------------------------
def db_test():
    DB = sql.connect(database= os.path.join(os.pardir,'data',"TestDB.db"))
    cur = DB.cursor()
    cur.execute('SELECT sqlite_version()')
    print(cur.fetchone()[-1])


db_test()

#look into this https://stackoverflow.com/questions/71362727/python-sqlite3-insert-data-from-for-loop
