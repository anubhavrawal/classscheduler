from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name='scheduler-home'),
    path("home_api", views.home_api, name='home_api'),
    path("semester", views.semester_view, name="semView"),
    path("saveSemster", views.saveSemester, name='saveSemester'),
    path("rooms", views.room_page, name="scheduler-rooms"),
    path("saverooms", views.saveroom, name="saveRoom"),
    path("saveInstructor", views.saveInstructor, name="saveInstructor"),
    path("upload", views.upload_view, name="fileUpload"),
    path("instructors", views.instructor_page, name="scheduler-instructors"),
        path("saveInstructor",views.saveInstructor, name ="saveInstructor"),
    path("help", views.help_page, name="scheduler-help"),
    path("upload", views.upload_view, name="scheduler-upload"),
    path("saveTime", views.saveMeetingTime, name="saveMeetingTime"),
    path("meeting_times", views.meeting_times_page,
         name="scheduler-meeting-times"),
]
