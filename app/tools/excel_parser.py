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
#df.columns = map(str.lower, df.columns)
df = df.drop(columns=['Unnamed: 18'])

new = list(df.columns)
#print (new)
#excel_col = new[0:17] +['Day/Time']+ new[21:26]
excel_col =  new[0:17] +['Begin Date',"End Date"]+ new[21:26]+ ["Meeting Time","Department"]

print(excel_col)


data=cur.execute('''SELECT * FROM scheduler_semester''')
print([col[0] for col in data.description][1:])

data=cur.execute('''SELECT * FROM scheduler_header_map''')
#print([col[0] for col in data.description][1:])

'''
df2 = pd.read_excel(path, 
                    sheet_name= 'CS',
                    header=3,
                    usecols='Q:W',
                    skipfooter=2,
                    dtype={'Shed Type':'object'} )
'''
#df = df.dropna(axis=0, how='all')


#df.to_sql(name='test', con =conn)

#df3 = pd.read_sql('select * from scheduler_semester', conn)
#df.at[0, 'crn'] = 12
#print(df.head())


#scheduler_semester
conn.close()

