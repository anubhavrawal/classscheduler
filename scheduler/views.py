from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from scheduler.models import Instructors
from scheduler.models import fields

coloumns =[
    'class',
    'room',
    'location',
    'credits',
    'hours'
]


data2 = list(Instructors.objects.values_list())
colums_info = fields(Instructors)

data = [
    {
        'class':"Computer Science 1",
        'room':"C100",
        'time':"1400",
        'location':"Parkview",
        'credits':"3",
        'hours': "3"
    },
    {
        'class':"Databases",
        'room':"D208",
        'time':"1100",
        'location':"Parkview",
        'credits':"4",
        'hours': "4"
    }
]

# Create your views here.
def main_page(request):
    context = {
        'input': data2,
        'col': colums_info
    }
    return render(request, 'scheduler/home.html', context)

def room_page(request):
    context = {

    }
    return render(request, 'scheduler/rooms.html', context)
