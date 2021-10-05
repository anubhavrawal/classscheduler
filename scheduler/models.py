import builtins
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, TextField
from django.db.models.fields.json import JSONField

# Create your models here.
class Semester(models.Model):

    # All of the items that create a semester
    crn = models.IntegerField(unique = True)
    dept = models.CharField(max_length= 4)
    course_id = models.CharField(max_length=9)
    section = models.IntegerField()
    status = models.CharField(max_length= 1)
    title = models.TextField()
    link1 = models.CharField(max_length=2)
    link2 = models.CharField(max_length=2)
    schedule_type = models.CharField(max_length=2)
    reserved = models.CharField(max_length=1)
    credit_hours = models.IntegerField()
    billing_hours = models.IntegerField()
    contact_hours = models.IntegerField()
    grad_able = models.CharField(max_length=1)
    cap = models.IntegerField()
    waitlist_cap = models.IntegerField()
    spec_appr = models.CharField(max_length=5)
    meeting_type = models.CharField(max_length= 5)
    begin_date = models.DateField()
    end_date = models.DateField()
    days = models.CharField(max_length=8)                               # Check to make sure time and days exist in meeting_time
    time = models.IntegerField()                                        # Check for valid time in meeting_time
    location = models.IntegerField()                                    # Check for valid location in location table
    site_code = models.CharField(max_length=5)
    primary_instructor = models.IntegerField()                          # Check for valid teacher in teacher table
    fee = models.IntegerField()
    comment = models.TextField()

# Meeting times table
class Meeting_Times(models.Model):

    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.CharField(max_length=8)

# Rooms table
class Rooms(models.Model):
    #department =  models.TextField()
    campus = models.TextField()
    building = models.TextField()
    room_num = models.TextField()
    capacity = models.IntegerField()
    room_type = models.CharField(max_length=3)

# Instructors table
class Instructors(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    status = models.CharField(max_length=2)
    department = models.CharField(max_length=4)
    schedule = models.JSONField()

def fields(self):
    return [ f.name for f in self._meta.fields + self._meta.many_to_many ]


'''
class Column_Names (modes.Model):
    page_name = models.TextField()
    column_name = models.TextField()
    modeified_date = models.DateField()


'''