import openpyxl
import pandas as pd
from pathlib import Path
import sqlite3

conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()

DATA_DIR =  Path.cwd() / 'tools'
# Give the location of the file
path = DATA_DIR / "./demo.xlsx"
df = pd.read_excel(path, 
                    sheet_name= 'CS',
                    header=4,
                    usecols='A:AA',
                    skipfooter=2,
                    dtype={'Shed Type':'object'} )
df.columns = map(str.lower, df.columns)

df = df.drop(columns=['unnamed: 18'])

#df = df.dropna(axis=0, how='all')


#df.to_sql(name='test', con =conn)

#df3 = pd.read_sql('select * from scheduler_semester', conn)
#df.at[0, 'crn'] = 12
#print(df.head())
# for col in df.columns:
#     print(col)
#print(df['unnamed: 18'])

entries = 0
classes = []
temp = []

for index, row in df.iterrows():
    if(not pd.isna(row['crn'])):
        entries += 1
        
    else:
        entries += 0


print(entries)

#scheduler_semester
conn.close()

