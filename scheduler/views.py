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
from .constants import *
from django.db import connection
from collections import namedtuple
import json
from django.core import serializers

import io
from rest_framework.parsers import JSONParser

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def main_page(request):
    items = ''
    edit = "false"
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM "+ semester_table)
        items = namedtuplefetchall(cursor)

        context = {
            'input': items,
            'col': "id",  #fields(Semester)[1:]
            'edit_mode': edit,
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

def saveroom(request):
    if request.method== "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        tmpResp = Roomsserializer(data = data[0])

        for val in data:
            saveserialize = Roomsserializer(data = val)
            if saveserialize.is_valid():
                saveserialize.save()
                #return Response(saveserialize.data, status= status.HTTP_201_CREATED)
            else:
                return Response(saveserialize.data, status= status.HTTP_400_BAD_REQUEST)
        
        return Response(saveserialize.data, status= status.HTTP_201_CREATED)    
    

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
