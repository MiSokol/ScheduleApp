from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Task

def task_list(request):
    return HttpResponse("Main Page")

def login(request):
    return HttpResponse("Login Page")

def settings(request):
    return HttpResponse("Settings Page")
