# Requirements

<hr>

## from meeting with Dr. Carr (3/10/2021)

 - Must haves: 

	- The system must contain a basic authentication system. 

		- Viewer (Can only see classes and schedule) 

		- Administrator (Can change classes in their specified department) 

		- Super user (Can change or modify courses in any department) 

	- The home screen with have the details on the class scheduling information, instructor, course, time.  

	- The information will be imported from a xlsx file. 

	- Be able to view by instructor what course they are teaching. 

	- Export all the information to excel file. 

	- Before the information is saved to the database, they must pass the set rules (Time/Instructor/Location conflicts) 

- Wish list: 

	- Be able to make changes dynamically to multiple lines in the edit mode. 

	- Filter all courses on main page by any of their keys. 

<hr>

## from submitted requirements doc (4/30/2021)

- Arrival:  

	- User login and authentication  

	- 3 types of users possible  

		- Base level users with permission to only view the database for their department specified.  

		- Department administrators can change data in the department.  

		- Superuser can assign privileges and change anything throughout the entire system.  

- Inside Application:  

	- Import to the database from a .xlsx file.  

	- View all the classes with their respective categories.  

	- Select which categories for the classes can be shown on the screen.  

	- Ability to filter the list by any of the categories chosen.  

	- Superusers can dynamically change the information on the classes.  

	- Error checking will be implemented so that no teacher has multiple classes at the same time or so no classes will be in the same room at the same time.  

	- Users can then look up any teacher and see their schedule.  

	- Finally, after the schedule for the semester is well represented, the user can export to a .xlsx file. 

# Installation Commands

- Make sure that the linux system is uptodate

	```
	sudo apt update
	sudo apt upgrade
	```

- Install Python3

	```
	sudo apt-get install python3
	```

- Install mySqlserver

	```
	sudo apt-get install mysql-server
	```

- Install the python3 SQL client dependencies

	```
	sudo apt install python3 libmysqlclient-dev default-libmysqlclient-dev
	```

- Install all python dependencies

	```
	pip3 install -r requirements.txt
	```