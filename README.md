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

## Run

```
$ python manage.py runserver 0.0.0.0:8080
```

## Installation Guidelines

- Make sure that the linux system is uptodate

	```
	$ sudo apt update
	$ sudo apt upgrade
	```

- Install Python3

	```
	$ sudo apt-get install python3
	```

- Install mySqlserver

	```
	$ sudo apt-get install mysql-server
	```

- Install the python3 SQL client dependencies

	```
	$ sudo apt install python3 libmysqlclient-dev default-libmysqlclient-dev
	```

- Install all python dependencies

	```
	$ pip3 install -r requirements.txt
	```
- Importing a database
	```
	mysql> CREATE database SCHEDULER;
	
	$ mysql SCHEDULER <scheduler.db
	$ sudo apt-get install python3-dev
	```


- Dumping a database
	```
	$ mysqldump SCHEDULER > scheduler.db
	```
- Create a user
	```
	mysql> CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
	mysql> GRANT ALL ON SCHEDULER.* TO 'djangouser'@'%';
	mysql> FLUSH PRIVILEGES;
	```

## Run Guidelines

- Start the mysqlserver in the local system
    ```
    $ sudo service mysql start
    ```
- Start the django server
    ```
    $ python3 manage.py runserver
    ```
	
# Deploy

	```
	$ sudo apt-get install python3-setuptools libpython-dev python3-dev
	$ sudo apt-get install nginx
	$ sudo apt-get install uwsgi uwsgi-plugin-python3
	
	#Start the server with uwsgi
	$uwsgi --socket Class_Scheduler.sock --module Class_Scheduler.wsgi --chmod-socket=666
	$sudo /etc/init.d/nginx restart #To restart nginx
	```
-Test:
	```
	$ uwsgi --ini Class_Scheduler_uwsgi.ini
	```

- Run server guidelines
	```
	python manage.py runserver 0.0.0.0:8080
	```

# Deploy2

	```
	$ sudo apt-get install python3-setuptools libpython-dev python3-dev
	$ sudo apt-get install nginx
	$ sudo apt-get install uwsgi uwsgi-plugin-python3
	
	#Start the server with uwsgi
	$uwsgi --socket Class_Scheduler.sock --module Class_Scheduler.wsgi --chmod-socket=666
	$sudo /etc/init.d/nginx restart #To restart nginx
	```
-Test:
	```
	$ uwsgi --ini Class_Scheduler_uwsgi.ini
	```

- Run server guidelines
	```
	python manage.py runserver 0.0.0.0:8080
	```

# Create a Virtual environment
	```
	$ sudo apt install virtualenv -y
	$ virtualenv <envname> -p  python3
	$
	```