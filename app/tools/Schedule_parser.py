import pandas as pd
from pathlib import Path
import datetime
from sqlalchemy import create_engine
import math

### Variables ###
classes = []
temp = [] 
temp_days = ''
temp_times = ''
day_col = 19
time_col = 20
comment_col = 24

### Methods ###
def adjust_instructors(conn, line):

    # Make sure that there is a name
    if(pd.isna(line)):
        line = ""

    # Split name at the space character
    names = line.split(" ")

    # If there was a name then run sql to find the id of who it is.
    if(len(names) > 1):
        instructors_df = pd.read_sql("SELECT first_name, last_name, id FROM scheduler_instructors WHERE first_name ='"+ names[0] +"' AND last_name ='"+names[1] + "';", conn)
        
        # If a name was found assign that id to the primary instructor spot
        if(not instructors_df.empty):
            temp[21] = (instructors_df['id'].values[0])
        
        # if empty then append 1
        else:
            temp[21] = 1
    else:
        temp[21] = 1   

    return

def adjust_meeting_times(conn, days,time):

    # if days are NAN then make them into an empty string
    if(pd.isna(days)):
        days = ""
    
    # if time is NAN then make it into an empty string
    if(pd.isna(time)):
        time = ""
    
    # split the time at the ('-') character to get start and end time
    time = time.split('-')
    
    # As long as the time was able to be split then find the corresponding time in the table
    if(len(time) > 1):

        # Format the two times into the correct strings
        time[0] = str(datetime.datetime.strptime(time[0], "%H%M"))
        time[1] = str(datetime.datetime.strptime(time[1], "%H%M"))

        # If days is not empty then search for the correct day and time
        if(days != ""):
            result =  pd.read_sql("SELECT TIME(start_time) AS start_time, TIME(end_time) AS end_time, days, id FROM scheduler_meeting_times "+ 
                                    "WHERE start_time = + '"+ time[0] +"' "+ 
                                    "AND end_time = '"+time[1]+"' "+
                                    "AND days = '"+ days +"'; ", conn)

        # If days is empty, then search for the correct time
        else:
            result =  pd.read_sql("SELECT TIME(start_time) AS start_time, TIME(end_time) AS end_time, days, id FROM scheduler_meeting_times "+ 
                                    "WHERE start_time = + '"+ time[0] +"' "+ 
                                    "AND end_time = '"+time[1]+"';", conn)

        # If there was no result then add default value of 1
        if(result.empty):
            temp[24] = 1
        else:
            temp[24] = result['id'].values[0]
    else:
        temp[24] = 1
    return

def adjust_room(conn, line):

    # if the line is Not a Number(NAN) set it to default line(0000)
    if(pd.isna(line)):
        line = "0000"

    # Run an sql statement to find the room number in the table
    rooms_df = pd.read_sql("SELECT room_num, building, id FROM scheduler_rooms WHERE room_num ='" +line[0:4]+"';", conn)
    
    # If something was found, input the id of the room in temp. if not input id of default in
    if(not rooms_df.empty):
        temp[19] = (rooms_df['id'].values[0])
    else:
        temp[19] = 1
    return

def adjust_dates(line):

    # split the dates at the ('-') character so you have beginning date and end date
    dates = line.split('-')
    temp[17] = (datetime.datetime.strptime(dates[0], "%m/%d").date())                   # Appends Start date
    temp[18] = (datetime.datetime.strptime(dates[1], "%m/%d").date())                   # Appends End date
    return

import pymysql.cursors
import pymysql

def semParser (semesterName, department, content):
    global classes
    global temp
    global temp_days
    global temp_times

    ### Database connection ###
    # format: engine = sqlalchemy.create_engine('mysql://user:password@server') #
    engine = create_engine("mysql://djangouser:password@127.0.0.1/SCHEDULER")
    conn = engine.connect()

    #cur = conn.cursor()

    DATA_DIR =  Path.cwd() / 'tools'
    # Give the location of the file
    path = DATA_DIR / "./demo.xlsx"
    df = pd.read_excel(content.file, 
                        sheet_name= 'CS',
                        header=4,
                        usecols='A:AA',
                        skipfooter=2,
                        dtype={'Shed Type':'object'} )

    df = df.drop(columns=['Unnamed: 18'])
    tmp_col_list = list(df.columns)
    df.columns = map(str.lower, df.columns)

    #---------------------------Formating header for header_map db---------------------------
    excel_col =  tmp_col_list[0:17] +['Begin Date',"End Date"]+ tmp_col_list[21:26]+ ["Meeting Time","Department"]
    db=conn.execute('''SELECT * FROM scheduler_semester''')

    tmp_db =  list(db.keys())[1:-1]
    print(excel_col)
    print(len(excel_col))
    
    db_col_list = ['crn'] + tmp_db[2:20]+ tmp_db[21:26] + ['meet_time','dept', 'season_year']
    print(db_col_list)
    print(len(db_col_list))
    
    '''
    header_map_df = pd.DataFrame()
    header_map_df.insert (0, "PageName", ['scheduler_semester'] * len(excel_col))
    header_map_df.insert (1, "CSVheader", excel_col )
    header_map_df.insert (1, "DBheader", db_col_list )
    '''
    #print("Processing excel header information")
    
    '''
    try:
        header_map_df.to_sql(name='scheduler_header_map',if_exists='append', index_label='id', con =conn)
        print("Sucessfully Added excel header information")
    except Exception as e :
        print("Failed to add excel header information to database....\n Error Message: " + str(e) )
    '''
    
    #--------------------------------Formatting End here-----------------------------------------

    ### Parser ###
    temp = ['']*27
    # Loop through each row in the content table 
    for index, row in df.iterrows():
        
        # Check for an actual CRN in the row
        if(not pd.isna(row['crn'])):

            # If it is not the first index, then append the temporary to the classes
            if(index > 0):

                # Get the correct meeting time with the days and time
                adjust_meeting_times(conn, temp_days, temp_times)

                # Find any NANs and remove them
                for x in range(len(temp)):
                    if pd.isna(temp[x]):
                        temp[x] = ''

                # Add to the schedule
                classes.append(temp)

                # Reset variables used
                temp = [''] * 27
                temp_days = ''
                temp_times =''

            # Enter the static pieces that wont change
            temp[0]  = row['crn']
            temp[1]  = row['course id']
            temp[2]  = row['section']
            temp[3]  = row['status']
            temp[4]  = row['title']
            temp[5]  = row['link1']
            temp[6]  = row['link2']
            temp[7]  = row['sched type']
            temp[8]  = row['rsvrd']
            temp[9]  = row['credit hours']
            temp[10] = row['billing hours']
            temp[11] = row['contact hours']
            temp[12] = row['grad- able']
            temp[13] = row['cap']
            temp[14] = row['waitlist cap']
            temp[15] = row['spec appr']
            temp[16] = row['mtg type']
            temp[20] = row['site code']
            temp[22] = row['fee']
            temp[23] = row['comment']
            temp[25] = department
            temp[26] = semesterName

            # Get begin date and end date from the dates
            adjust_dates(row['dates'])

            # Get correct location
            adjust_room(conn,row['location'])

            # Get Instructor
            adjust_instructors(conn, row['primary instructor'])

            # Set temp days if not empty
            if(not pd.isna(row['days'])):
                temp_days = row['days']
            else:
                temp_days = ''

            # Set temp time if not empty
            if(not pd.isna(row['time'])):
                temp_times = row['time']
            else:
                temp_times = ''

        # If the same CRN as last, then append the days and append the comment
        else:

            # Check to see if there is extra days in following lines
            if(not pd.isna(row['days'])):
                temp_days = str(temp_days) + str(row['days'])

            # Add any extra comments
            if(not pd.isna(row['comment'])):
                temp[23] = str(temp[23])+ " " +  str(row['comment'])

        # Checks the for the last entry to make sure that it wasn't an extra line and appends data to the classes list
        if(index == len(df)-1 and not pd.isna(row['crn'])):
            adjust_meeting_times(conn,temp_days, temp_times)
            classes.append(temp)
    
    new_df = pd.DataFrame(classes, columns=db_col_list)

    #new_df = new_df.reset_index()
    #print(new_df.columns)
    
    print("Processing excel header information")
    try:
        new_df.to_sql(name='scheduler_semester', if_exists='append' , index_label='id', index= False, con =conn)
        print("Sucessfully Added ")
    except Exception as e :
        print("Failed to add excel information to database....\n Error Message: " + str(e) )
    
    #scheduler_semester
    conn.close()

