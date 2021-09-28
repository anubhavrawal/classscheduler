import openpyxl
import pandas as pd
from pathlib import Path

DATA_DIR =  Path.cwd() / 'tools'
# Give the location of the file
path = DATA_DIR / "./demo.xlsx"
df = pd.read_excel(path, 
                    sheet_name= 'CS',
                    header=4,
                    usecols='A:Z',
                    skipfooter=2,
                    dtype={'Shed Type':'object'} )

df2 = pd.read_excel(path, 
                    sheet_name= 'CS',
                    header=3,
                    usecols='Q:W',
                    skipfooter=2,
                    dtype={'Shed Type':'object'} )

df = df.dropna(axis=0, how='all')
print(df.tail())


