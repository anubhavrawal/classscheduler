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

classes = []
temp = []
dayCol = 19
commentCol = 25

# Loop through each row in the content table 
for index, row in df.iterrows():

    # Check for an actual CRN
    if(not pd.isna(row['crn'])):
        classes.append(temp)
        temp = []

        # Iterate through each column in the courses and add it to the temporary class
        for col in range(len(row)):
            if(not pd.isna(row[col])):
                temp.append(row[col])
            else:
                temp.append("")
    
    # If the same CRN as last, then append the days and append the comment. Col 19 is rows, col 25 is comment
    else:

        # Add any extra days
        if(not pd.isna(row['days'])):
            temp[dayCol] = str(temp[dayCol]) + str(row['days'])

        # Add any extra comments
        if(not pd.isna(row[commentCol])):
            temp[commentCol] = str(temp[commentCol]) + " " +  str(row[commentCol])

#classes[0] = [""]
#df = pd.DataFrame(classes[1:], columns=classes[0])
#print(classes)

#scheduler_semester
conn.close()

