from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'instruments/main.html')

def instruments(request):
    return render(request, 'instruments/instruments.html')

def about(request):
    return HttpResponse('about')