import openpyxl
import pandas as pd
from pathlib import Path
import sqlite3


conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()

df = pd.read_sql('select * from scheduler_instructors', conn) #scheduler_rooms scheduler_meeting_times

df.to_excel("instructor.xlsx")


conn.close()