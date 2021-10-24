from django.contrib import admin
from.models import Instructors, Meeting_Times, Rooms, Semester

# Register your models here.

admin.site.register(Instructors)
admin.site.register(Rooms)
admin.site.register(Semester)
admin.site.register(Meeting_Times)