from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.task_list, name="task_list"),
    path("login/", views.login, name="login"),
    path("settings/", views.settings, name="settings"),
]
