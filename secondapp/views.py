from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse(f'<h1> welcome to home app function</h1>')


def app_home(request):
    return HttpResponse(f'<h1> welcome to home application function</h1>')


def work_fun(request):
    return HttpResponse(f'<h1> welcome to home work of the website application function</h1>')