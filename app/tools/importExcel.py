import openpyxl
import pandas as pd
from pathlib import Path
import sqlite3
import mysql.connector
from sqlalchemy import create_engine

engine = create_engine("mysql://djangouser:password@127.0.0.1/SCHEDULER")
conn = engine.connect()

DATA_DIR =  Path.cwd() / 'Extras'
# Give the location of the file
path = DATA_DIR / "./instructor.xlsx"
df = pd.read_excel(path, 
                    sheet_name= 'Sheet1',
                    header=0,
                    usecols='C:F')

df.to_sql(name='scheduler_instructors',if_exists='append', index_label='id', con =conn)



conn.close()