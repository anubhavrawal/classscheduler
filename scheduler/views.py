from django.shortcuts import render

# Create your views here.
def main_page(request):
    context = {

    }
    return render(request, 'scheduler/home.html', context)
