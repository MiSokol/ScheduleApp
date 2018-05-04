from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User, Task


def check_auth(request):
    try:
        cookies = request.session['login']
        if len(User.objects.filter(login=cookies)) > 0:
            return True
        else:
            return False
    except KeyError:
        return False


#Authorization
def login(request):
    return render(request, "scheduleapp/login_page.html")

def check_login(request):
    input_login = request.POST["login"]
    if len(User.objects.filter(login=input_login)) > 0:
        request.session['login'] = input_login
        return redirect("/")
    else:
        return redirect("/login/")

def logout(request):
    request.session["login"] = "NULL"
    return redirect("/login/")


#Main
def task_list(request):
    if not check_auth(request):
        return redirect("/login/")

    return render(request, "scheduleapp/main_page.html")

def settings(request):
    if not check_auth(request):
        return redirect("/login/")

    return HttpResponse("Settings Page")
