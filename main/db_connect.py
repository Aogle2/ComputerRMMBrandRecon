import os
import sqlite3 as sql
from pathlib import Path

def db_connect(filepath=os.path.join(os.pardir,'Data',"TestDB.db")):
    if Path(filepath):
        print("thisfile exist")


db_connect()