from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .models import fields


def main_page(request):
    context = {
        # 'input': Semester.objects.all(),
        # 'col': fields(Semester)[1:]
    }
    return render(request, 'scheduler/home.html', context)


def room_page(request):
    context = {
        'input': Rooms.objects.all(),
        'col': list(Header_Map.objects.filter(PageName = "scheduler_rooms").values_list('CSVheader', flat='True'))
    }
    return render(request, 'scheduler/rooms.html', context)


def instructor_page(request):
    context = {
        'input': Instructors.objects.all(),
        'col': fields(Instructors)[1:]
    }
    return render(request, 'scheduler/instructors.html', context)
