import openpyxl
import pandas as pd
from pathlib import Path
#import sqlite3
#import mysql.connector
from sqlalchemy import create_engine

'''
conn =  mysql.connector.connect(user='djangouser', password='password',
                              host='127.0.0.1',
                              database='SCHEDULER')
'''
engine = create_engine("mysql://djangouser:password@127.0.0.1/SCHEDULER")
conn = engine.connect()

DATA_DIR =  Path.cwd() / 'Extras'
# Give the location of the file
path = DATA_DIR / "./timeslots.xlsx"
df = pd.read_excel(path, 
                    sheet_name= 'timeslots',
                    header=0,
                    usecols='A:C')

#df.columns = map(str.lower, df.columns)
df = df.rename(columns={"Start": "start_time", "End": "end_time", "Days": "days"})

df.to_sql(name='scheduler_meeting_times',if_exists='append', index_label='id',index= False, con =conn)
df3 = pd.read_sql('select * from scheduler_meeting_times', conn) #scheduler_rooms scheduler_meeting_times
conn.close()

print(df3.head())