# Class Scheduling Web Application in Django

Senior Design Project  
WMU CS4910  
Fall 2021

### Authors
Michael Coffey  
Altan Rawal  
Brenden Rasmussen

## Description
An application that allows users to schedule classes and view the schedule of classes that have been scheduled.


# Installation Guidelines

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
- Dumping a database
	```
	mysqldump SCHEDULER > scheduler.db
	```
- Create a user
	```
	mysql> CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
	mysql> GRANT ALL ON SCHEDULER.* TO 'djangouser'@'%';
	mysql> FLUSH PRIVILEGES;
	```
- 