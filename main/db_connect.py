import os
import sqlite3 as sql
from pathlib import Path

def file_check(func):
    filepath= os.path.join(os.pardir,'Data',"TestDB.db")
    if Path(filepath):
        print("thisfile exist 1")


@file_check #Overview here: https://realpython.com/primer-on-python-decorators/
def test():
    print("Test 2")



#--------------------------------------------------

def db_test():
    DB = sql.connect(database= os.path.join(os.pardir,'Data',"TestDB.db"))
    cur = DB.cursor()
    cur.execute('SELECT sqlite_version()')
    print(cur.fetchone()[-1])


db_test()
