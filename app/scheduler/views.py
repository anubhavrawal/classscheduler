from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .serialize import Roomsserializer, Instructorserializer, MeetingTimeserializer, Semesterserializer, Homeserializer
from .models import *
from .models import fields
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from rest_framework.permissions import AllowAny
from tools.Schedule_parser import semParser

from .constants import *
from django.db import connection
from collections import namedtuple

from .models import Rooms, Instructors
from .forms import UploadFileForm

import io
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import APIException
from dateutil import tz
from django.http import HttpResponseRedirect
import json


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def main_page(request):
    if request.POST:
        form = UploadFileForm(request.FILES)
        if form.is_valid():
            semParser('test', request.FILES.get('File_field'))
    else:
        form = UploadFileForm()

    # items = ''
    # edit = "false"
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM " + semester_table)
    context = {
        'input': Semester.objects.values('season_year').distinct()

    }
    return render(request, 'scheduler/home.html', context)


@api_view(('DELETE',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@permission_classes([AllowAny])
def home_api(request):
    if request.method == 'DELETE':
        saveserialize = Homeserializer(data=request.data)
        #response = {'status': 1, 'message':"Internal Server Error", 'url':'/rooms'}

        if saveserialize.is_valid():
            tmp = saveserialize.delete(
                saveserialize.validated_data)  # perform the action
            return Response(tmp.data)
        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
def semester_view(request):
    items = ''
    edit = "false"
    term = request.GET['term']
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM " + semester_table +
                       " Where season_year = '"+term+"'")
        items = namedtuplefetchall(cursor)

        context = {
            'input': items,
            'col': "id",  # fields(Semester)[1:]
            'edit_mode': "false",
        }
        context['form'] = UploadFileForm()

        return render(request, 'scheduler/home.html', context)


def upload_view(request):
    context = {}
    if request.POST:
        form = UploadFileForm(request.FILES)
        if form.is_valid():
            semParser('test', request.FILES.get('File_field'))
    else:
        form = UploadFileForm()

    context['form'] = UploadFileForm()

    return render(request, "scheduler/upload.html", {'form': form})


@api_view(('POST', 'DELETE',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def saveInstructor(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        saveserialize = Instructorserializer(data=data, many=True)

        if saveserialize.is_valid():
            saveserialize.update(Instructors, saveserialize.validated_data)
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)

    # Handel the delete functionality
    if request.method == "DELETE":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        pk = data['id']  # fetch primary key to deleate

        saveserialize = Instructorserializer(data=data)


@permission_classes([AllowAny])
def saveSemester(request):
    if request.method == "POST":
        saveserialize = Roomsserializer(data=request.data, many=True)

        if saveserialize.is_valid():
            saveserialize.update(Rooms, saveserialize.validated_data)
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        saveserialize = Semesterserializer(data=request.data)
        pk = int(request.query_params['id'])

        if saveserialize.is_valid():
            # perform the action
            saveserialize.delete(saveserialize.validated_data, pk)
            return Response(pk, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST', 'DELETE',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def saveroom(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        saveserialize = Roomsserializer(data=data, many=True)

        if saveserialize.is_valid():
            saveserialize.update(Rooms, saveserialize.validated_data)
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)

    # Handel the delete functionality
    if request.method == "DELETE":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        pk = data['id']  # fetch primary key to deleate

        saveserialize = Roomsserializer(data=data)

        if saveserialize.is_valid():
            # perform the action
            saveserialize.delete(saveserialize.validated_data, pk)
            return Response(pk, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST', 'DELETE',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def saveroom(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        saveserialize = Roomsserializer(data=data, many=True)

        if saveserialize.is_valid():
            saveserialize.update(Rooms, saveserialize.validated_data)
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)


def room_page(request):
    context = {
        'input': Rooms.objects.all(),
        'col': list(Header_Map.objects.filter(PageName="scheduler_rooms").values_list('CSVheader', flat='True'))
    }
    return render(request, 'scheduler/rooms.html', context)


def instructor_page(request):
    context = {
        'input': Instructors.objects.all()[1:],
        'col': fields(Instructors)[1:]
    }
    return render(request, 'scheduler/instructors.html', context)


@api_view(('POST', 'DELETE',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def saveInstructor(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        saveserialize = Instructorserializer(data=data, many=True)

        if saveserialize.is_valid():
            saveserialize.update(Instructors, saveserialize.validated_data)
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)

    # Handle the delete functionality
    if request.method == "DELETE":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        pk = data['id']  # fetch primary key to delete

        saveserialize = Instructorserializer(data=data)

        if saveserialize.is_valid():
            resp = saveserialize.delete(
                saveserialize.validated_data, pk)  # perform the action
            return Response(resp, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)


def room_page(request):
    context = {
        'input': Rooms.objects.all(),
        'col': list(Header_Map.objects.filter(PageName="scheduler_rooms").values_list('CSVheader', flat='True'))
    }
    return render(request, 'scheduler/rooms.html', context)


def instructor_page(request):
    context = {
        'instructors': Instructors.objects.all()[1:],
        'col': fields(Instructors)[1:]
    }
    return render(request, 'scheduler/instructors.html', context)


def help_page(request):
    return render(request, 'scheduler/help.html')


# def upload_page(request):
#     return render(request, 'scheduler/upload.html')


def meeting_times_page(request):
    context = {
        'input': Meeting_Times.objects.all(),
        'temp': list(Meeting_Times.objects.all())[1],
        'col': fields(Meeting_Times)[1:]
    }
    return render(request, 'scheduler/meeting_times.html', context)


@api_view(('POST', 'DELETE',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def saveMeetingTime(request):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    if request.method == "POST":
        for info in request.data:
            tmpdate = datetime.fromisoformat(
                info['start_time'][:-1]).replace(tzinfo=from_zone).astimezone(to_zone)
            info['start_time'] = tmpdate.strftime('%H:%M:%S')
            tmpdate = datetime.fromisoformat(
                info['end_time'][:-1]).replace(tzinfo=from_zone).astimezone(to_zone)
            info['end_time'] = tmpdate.strftime('%H:%M:%S')

        saveserialize = MeetingTimeserializer(data=request.data, many=True)

        if saveserialize.is_valid():
            saveserialize.update(Meeting_Times, saveserialize.validated_data)
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)

    # Handel the delete functionality
    if request.method == "DELETE":

        # fetch primary key to deleate
        pk = request.data['id']
        tmpdate = datetime.fromisoformat(
            request.data['start_time'][:-1]).replace(tzinfo=from_zone).astimezone(to_zone)
        request.data['start_time'] = tmpdate.strftime('%H:%M:%S')
        tmpdate = datetime.fromisoformat(
            request.data['end_time'][:-1]).replace(tzinfo=from_zone).astimezone(to_zone)
        request.data['end_time'] = tmpdate.strftime('%H:%M:%S')

        saveserialize = MeetingTimeserializer(data=request.data)

        if saveserialize.is_valid():
            # perform the action
            saveserialize.delete(saveserialize.validated_data, pk)
            return Response(pk, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(saveserialize.error_messages, status=status.HTTP_400_BAD_REQUEST)
