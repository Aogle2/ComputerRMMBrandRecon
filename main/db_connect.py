import os
import sqlite3 as sql
from pathlib import Path

def file_check(func):
    filepath= os.path.join(os.pardir,'Data',"TestDB.db")
    if Path(filepath):
        print("thisfile exist 1")
        print(func())


@file_check #Overview here: https://realpython.com/primer-on-python-decorators/
def test():
    print("Test 2")