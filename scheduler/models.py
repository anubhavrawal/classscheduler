# import builtins
from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.fields import CharField, TextField
# from django.db.models.fields.json import JSONField


    # All of the items that create a semester
class Semester(models.Model):
    crn = models.IntegerField(unique = True)
    course_id = models.CharField(max_length=9)
    section = models.IntegerField()
    status = models.CharField(max_length=1)
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
    meeting_type = models.CharField(max_length=5)
    begin_date = models.DateField()
    end_date = models.DateField()
    location = models.IntegerField()                                    # Check for valid location in location table
    site_code = models.CharField(max_length=5)
    primary_instructor = models.IntegerField()                          # Check for valid teacher in teacher table
    fee = models.IntegerField()
    comment = models.TextField()
    meet_time = models.IntegerField()                                   # Check for valid time in meeting_time
    dept = models.CharField(max_length= 4)

class Meeting_Times(models.Model):  # Meeting times table

    start_time = models.TimeField('%H:%M')
    end_time = models.TimeField('%H:%M')
    days = models.CharField(max_length=8)


class Rooms(models.Model):  # Rooms table
    campus = models.TextField()
    building = models.TextField()
    room_num = models.TextField()
    capacity = models.IntegerField()
    room_type = models.CharField(max_length=3)


class Instructors(models.Model):  # Instructors table
    last_name = models.TextField()
    first_name = models.TextField()
    status = models.CharField(max_length=2)
    department = models.CharField(max_length=4)
    schedule = models.JSONField()


def fields(self):
    """
    gathers fields from the model and returns
    a dictionary of the fields and their values
    """
    return [f.name for f in self._meta.fields + self._meta.many_to_many]
