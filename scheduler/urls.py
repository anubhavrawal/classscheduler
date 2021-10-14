from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name='scheduler-home'),
    path("rooms", views.room_page, name="scheduler-rooms"),
    path("instructors", views.instructor_page, name="scheduler-instructors"),
]
