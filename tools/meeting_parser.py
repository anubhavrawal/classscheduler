import openpyxl
import pandas as pd
from pathlib import Path
import sqlite3
from sqlalchemy import create_engine


engine = create_engine("mysql://djangouser:password@127.0.0.1/SCHEDULER")
conn = engine.connect()

DATA_DIR =  Path.cwd() / 'Extras'
# Give the location of the file
path = DATA_DIR / "./combined.xlsx"
df = pd.read_excel(path, 
                    sheet_name= 'Rooms',
                    header=0,
                    usecols='A:E')



columns= {'Room#': 'room_num', 'Room Type': 'room_type', 'Building': 'building', 'Campus': 'campus', 'Capacity': 'capacity'}

excel_col = columns.keys()
db_col_list =  columns.values()

header_map_df = pd.DataFrame()
header_map_df.insert (0, "PageName", ['scheduler_rooms'] * len(excel_col))
header_map_df.insert (1, "CSVheader", excel_col )
header_map_df.insert (1, "DBheader", db_col_list )
print(header_map_df)


try:
    header_map_df.to_sql(name='scheduler_header_map',if_exists='append', index=False, con =conn)
    print("Sucessfully Added excel header information")
except Exception as e :
    print("Failed to add excel header information to database....\n Error Message: " + str(e) )

'''
df.rename(columns= columns, inplace=True)
try:
    df.to_sql(name='scheduler_rooms',if_exists='append', index_label='id',index= False, con =conn)
    print("Sucessfully Added excel information")
except Exception as e :
    print("Failed to add excel information to database....\n Error Message: " + str(e) )

#df3 = pd.read_sql('select * from scheduler_rooms', conn) #scheduler_rooms scheduler_meeting_times
'''

conn.close()

#print(df3.head())