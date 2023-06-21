"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalogo.views import home, pagina_api,pagina_cotiza,pagina_dulces,pagina_login,pagina_snacks,index
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index,name='home'),

    path('admin/', admin.site.urls),
    path('catalogo/',include('catalogo.urls')),
    path('usuario/', include('Usuario.urls')),


    
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),


    path('api/',pagina_api,name='pagina_api'),
    path('cotiza/',pagina_cotiza,name='pagina_cotiza'),
    path('dulces/',pagina_dulces,name='pagina_dulces'),
    path('login/',pagina_login,name='pagina_login'),
    path('snacks/',pagina_snacks,name='pagina_snacks'),
    path('snacks/',pagina_snacks,name='pagina_snacks'),
   
]
