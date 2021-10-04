import openpyxl
import pandas as pd
from pathlib import Path
import sqlite3
import sys


conn = sqlite3.connect("db.sqlite3")

cursor = conn.cursor()

mode = sys.argv[1]

if (mode ==  '-t' ):
    tables = pd.read_sql_query("SELECT * from sqlite_master WHERE type='table' ", conn)
    print(tables)

elif (mode== '-v'):
    table =  sys.argv[2]
    df3 = pd.read_sql('select * from '+ table, conn) #scheduler_rooms scheduler_meeting_times
    print(df3.head())

else:
    print("Usage: Python3 tools/database_lookup.py [-t] [-v] [tablename]")
    print("[-t] : shows all the tables in the database")
    print("[-v] [tablename]: shows few table for the given table")

conn.close()

