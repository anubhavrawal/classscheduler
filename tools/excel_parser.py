import openpyxl
import pandas as pd
from pathlib import Path
import sqlite3

def rand(x):
    return x

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



df2 = pd.read_excel(path, 
                    sheet_name= 'CS',
                    header=3,
                    usecols='Q:W',
                    skipfooter=2,
                    dtype={'Shed Type':'object'} )

df = df.dropna(axis=0, how='all')


#df.to_sql(name='test', con =conn)

#df3 = pd.read_sql('select * from scheduler_semester', conn)
#df.at[0, 'crn'] = 12
print(df.head())


#scheduler_semester
conn.close()

