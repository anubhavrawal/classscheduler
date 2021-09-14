from django.db import models

# Create your models here.
class Semester(models.Model):

    # All of the items that create a semester
    crn = models.IntegerField()
    course_id = models.CharField(max_length=20)
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
    meeting_type_desc = models.TextField()
    dates = models.TextField()
    days = models.CharField(max_length=2)
    time = models.TextField()
    location = models.TextField()
    site_code = models.CharField(max_length=5)
    primary_instructor = models.TextField()
    fee = models.IntegerField()
    comment = models.TextField()
