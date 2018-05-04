from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.task_list, name="task_list"),
    path("login/", views.login, name="login"),
    path("check_login/", views.check_login, name="check_login"),
    path("logout/", views.logout, name="logout"),
    path("settings/", views.settings, name="settings"),
]
