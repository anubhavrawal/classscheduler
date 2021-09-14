from django.shortcuts import render
from django.http import HttpResponse

coloumns =[
    'class',
    'room',
    'location',
    'credits',
    'hours'
]

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
        'input': data
    }
    return render(request, 'scheduler/home.html', context)
