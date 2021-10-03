from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name='scheduler-home'),
    path("rooms", views.room_page, name = "scheduler-rooms"),
]