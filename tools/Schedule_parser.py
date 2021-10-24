import openpyxl
import pandas as pd
from pathlib import Path
import sqlite3

### Variables ###
classes = []
temp = [] 
temp_days = ''
temp_times = ''
day_col = 19
time_col = 20
comment_col = 24

### Methods ###
def do_adjustment(col, line):
    if (col == 18):
        adjust_dates(line)
    elif (col == 21):
        adjust_room(line)
    else:
        adjust_instructors(line)

def adjust_department(line):
    temp.append(line[0:2])
    return

def adjust_instructors(line):
    if(pd.isna(line)):
        line = ""
    names = line.split(" ")

    if(len(names) > 1):
        instructors_df = pd.read_sql("SELECT first_name, last_name, id FROM scheduler_instructors WHERE first_name ='"+ names[0] +"' AND last_name ='"+names[1] + "';", conn)
        if(not instructors_df.empty):
            temp.append(instructors_df['id'].values[0])
        else:
            temp.append(1)
    else:
        temp.append(1)   

    return

def adjust_meeting_times(days,time):
    if(pd.isna(days)):
        days = ""
    if(pd.isna(time)):
        time = ""
    
    time = time.split('-')

    # Change format of the times to fit the model
    if(len(time) > 1):
        if(days != ""):
            meet_times_df = pd.read_sql("SELECT strftime('%H%M', start_time), strftime('%H%M',end_time), days, id FROM scheduler_meeting_times "+
                                        "WHERE strftime('%H%M', start_time) = '"+ time[0] +"' "+
                                        "AND strftime('%H%M', end_time) = '"+ time[1] +"' "+
                                        "AND days = '"+ days +"';",conn)
        else:
            meet_times_df = pd.read_sql("SELECT strftime('%H%M', start_time), strftime('%H%M',end_time), days, id FROM scheduler_meeting_times "+
                                        "WHERE strftime('%H%M', start_time) = '"+ time[0] +"' "+
                                        "AND strftime('%H%M', end_time) = '"+ time[1] +"';",conn)
        
        if(meet_times_df.empty):
            temp.append(0)
        else:
            temp.append(meet_times_df['id'].values[0])
       # meet_times_df = pd.read_sql("SELECT start_time, end_time, days, id FROM scheduler_meeting_times WHERE start_time LIKE 08:00:00;",conn)
    else:
        temp.append(0)

def adjust_room(line):
    if(pd.isna(line)):
        line = "0000"
    rooms_df = pd.read_sql("SELECT room_num, building, id FROM scheduler_rooms WHERE room_num ='" +line[0:4]+"';", conn)
    if(not rooms_df.empty):
        temp.append(rooms_df['id'].values[0])
    else:
        temp.append(0)
    #if(line[0:5] in rooms_df['room_num']):
    #   temp.append()   
    return

def adjust_dates(line):
    dates = line.split('-')
    temp.append(dates[0])                   # Appends Start date
    temp.append(dates[1])                   # Appends End date
    return

### Database connection ###
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

### Parser ###

# Loop through each row in the content table 
for index, row in df.iterrows():
    # Check for an actual CRN
    if(not pd.isna(row['crn'])):
        if(index != 0):
            adjust_meeting_times(temp_days, temp_times)
            temp_days = ""
            temp_times = ""
            adjust_department(temp[1])
            classes.append(temp)
        else:
            classes.append(temp)
        temp = []

        # Iterate through each column in the courses and add it to the temporary class
        for col in range(len(row)):
            
            
            if(col in [18,21,23]):                                                          # Check for dates, meeting_times, instructors, and location(18,21,23)
                do_adjustment(col,row[col])
            
            elif(col == 19):                                                                # Checks for the days column 
                if(not pd.isna(row[col])):
                    temp_days = row[col]
                else:
                    temp_days = ""

            elif(col == 20):                                                                # Checks for the times column
                if(not pd.isna(row[col])):
                    temp_times = row[col]
                else:
                    temp_times = ""

            elif(col == 17):                                                                # Skips the description of meeting type
                pass

            elif(not pd.isna(row[col])):                                                    # Appends information that are real values
                temp.append(row[col])

            else:                                                                           # If not a real value, then it will append an empty string in that place
                temp.append("")
    
    # If the same CRN as last, then append the days and append the comment. Col 19 is days, col 25 is comment
    else:

        # Add any extra days
        if(not pd.isna(row['days'])):
            temp_days = str(temp_days) + str(row['days'])

        # Add any extra comments
        if(not pd.isna(row[comment_col])):
            temp.append(str(temp[comment_col]) + " " +  str(row[comment_col]))
        
for row in classes:
    print(row)

#scheduler_semester
conn.close()


