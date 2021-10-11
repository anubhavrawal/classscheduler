from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name='scheduler-home'),
    path("scheduler/instructors/", views.instructors, name='scheduler-instructors'),
]
