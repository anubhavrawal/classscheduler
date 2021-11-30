import pandas as pd
from pathlib import Path
import datetime
from sqlalchemy import create_engine

### Variables ###
classes = []
temp = [] 
temp_days = ''
temp_times = ''
day_col = 19
time_col = 20
comment_col = 24

### Methods ###
def do_adjustment(conn, col, line):
    if (col == 18):
        adjust_dates(line)
    elif (col == 21):
        adjust_room(conn, line)
    else:
        adjust_instructors(conn,line)

def adjust_department(line):
    temp.append(line[0:2])
    return

def adjust_instructors(conn, line):
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

def adjust_meeting_times(conn, days,time):
    if(pd.isna(days)):
        days = ""
    if(pd.isna(time)):
        time = ""
    
    time = time.split('-')
    
    # Change format of the times to fit the model
    if(len(time) > 1):
        time[0] = str(datetime.datetime.strptime(time[0], "%H%M"))
        time[1] = str(datetime.datetime.strptime(time[1], "%H%M"))
        result = conn.execute("SELECT TIME(start_time) AS start_time, TIME(end_time) AS end_time, days, id FROM scheduler_meeting_times WHERE start_time = + '"+ time[0] +"' AND end_time = '"+time[1]+"' AND days = '"+ days +"';")

        if(days != ""):
            result =  conn.execute("SELECT TIME(start_time) AS start_time, TIME(end_time) AS end_time, days, id FROM scheduler_meeting_times "+ 
                                    "WHERE start_time = + '"+ time[0] +"' "+ 
                                    "AND end_time = '"+time[1]+"' "+
                                    "AND days = '"+ days +"'; ")
        else:
            result =  conn.execute("SELECT TIME(start_time) AS start_time, TIME(end_time) AS end_time, days, id FROM scheduler_meeting_times "+ 
                                    "WHERE start_time = + '"+ time[0] +"' "+ 
                                    "AND end_time = '"+time[1]+"';")
        
        if(not result):
            temp.append(1)
        else:
            for x in result:
                temp.append(x['id'])
    else:
        temp.append(1)
    return

def adjust_room(conn, line):
    if(pd.isna(line)):
        line = "0000"
    rooms_df = pd.read_sql("SELECT room_num, building, id FROM scheduler_rooms WHERE room_num ='" +line[0:4]+"';", conn)
    if(not rooms_df.empty):
        temp.append(rooms_df['id'].values[0])
    else:
        temp.append(1)
    return

def adjust_dates(line):
    dates = line.split('-')
    temp.append(datetime.datetime.strptime(dates[0], "%m/%d").date())                   # Appends Start date
    temp.append(datetime.datetime.strptime(dates[1], "%m/%d").date())                   # Appends End date
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
    # Loop through each row in the content table 
    for index, row in df.iterrows():
        # Check for an actual CRN
        if(not pd.isna(row['crn'])):
            if(index != 0):
                adjust_meeting_times(conn,temp_days, temp_times)
                temp_days = ""
                temp_times = ""
                adjust_department( temp[1])
                temp.append(semesterName)
                classes.append(temp)
            #else:
                #classes.append(temp)
            temp = []

            # Iterate through each column in the courses and add it to the temporary class
            for col in range(len(row)):
                
                
                if(col in [18,21,23]):                                                          # Check for dates, meeting_times, instructors, and location(18,21,23)
                    do_adjustment(conn, col,row[col])
                
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

    print( len(db_col_list) )
    #for row in classes:
    #    print(row)
    #print( [ ,excel_col, db_col_list] 
    
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
    
    print(classes[0][21])
    conn.close()
