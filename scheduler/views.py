from django.http import response
from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.models import User

from .serialize import Roomsserializer
from .models import *
from .models import fields

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .Schedule_parser import semParser

from .forms import UploadFileForm


def main_page(request):
    context = {
        # 'input': Semester.objects.all(),
        # 'col': fields(Semester)[1:]
    }
    return render(request, 'scheduler/home.html', context)

def upload_view(request):
    context = {}
    if request.POST:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            semParser('test',request.FILES.get('File_field'))
    else:
        form = UploadFileForm()

    context['form'] = UploadFileForm()
    return render(request, "scheduler/upload.html", context)

@api_view(['POST'])
def saveroom(request):
    if request.method== "POST":
        saveserialize = Roomsserializer(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data, status= status.HTTP_201_CREATED)
        else:
            return Response(saveserialize.data, status= status.HTTP_400_BAD_REQUEST)
    

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
