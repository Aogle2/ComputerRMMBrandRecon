import os
import sqlite3 as sql
import pathlib as path

def db_connect(filepath):
    if filepath.exist():
        print("thisfile exist")


for root in os.walk(os.join(os.pardir,'Data')):
    print(root)