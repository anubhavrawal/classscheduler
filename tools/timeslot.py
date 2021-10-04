import openpyxl
import pandas as pd
from pathlib import Path
import sqlite3


conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()

DATA_DIR =  Path.cwd() / 'Extras'
# Give the location of the file
path = DATA_DIR / "./timeslots.xlsx"
df = pd.read_excel(path, 
                    sheet_name= 'timeslots',
                    header=0,
                    usecols='A:E')

df.columns = map(str.lower, df.columns)

df.to_sql(name='scheduler_rooms',if_exists='append', index_label='id', con =conn)
df3 = pd.read_sql('select * from scheduler_rooms', conn) #scheduler_rooms scheduler_meeting_times
conn.close()

print(df3.head())