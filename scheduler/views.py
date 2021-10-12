from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from scheduler.models import Instructors, Rooms
from scheduler.models import fields

data2 = list(Instructors.objects.values_list())
colums_info = fields(Instructors)

# Create your views here.
def main_page(request):
    context = {
        'input': data2,
        'col': colums_info
    }
    return render(request, 'scheduler/home.html', context)

def room_page(request):
    context = {
        #'input': Rooms.objects.filter(
            #first_name__startswith='R'
            #).values('first_name', 'last_name')
        'input': Rooms.objects.all() ,
        'col': fields(Rooms)[1:]
    }
    return render(request, 'scheduler/rooms.html', context)
