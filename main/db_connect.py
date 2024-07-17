import os
import sqlite3 as sql
from pathlib import Path

def file_check(func,filepath=os.path.join(os.pardir,'Data',"TestDB.db")):
    if Path(filepath):
        print("thisfile exist")
        return filepath


@file_check
def test():
    print("Test")