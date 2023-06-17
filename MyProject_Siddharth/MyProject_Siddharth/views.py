from django.http import HttpResponse
from django.shortcuts import render


def greet(request):
    return HttpResponse("Hello There ! ")


def home(request):
    return render(request, 'home.html')


def child(request):
    return render(request, 'child.html')
