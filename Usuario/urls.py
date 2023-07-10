from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrar', views.RegistroUsuario, name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),
    
]
