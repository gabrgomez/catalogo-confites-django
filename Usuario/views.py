from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import RegistroForm

# class RegistroUsuario(CreateView):
#     model = User
#     template_name = "Usuario/registrar.html"
#     form_class = RegistroForm
#     success_url = reverse_lazy('list_user')
 
 
class UserList(ListView):
    model = User
    template_name = 'Usuario/list_user.html'

def RegistroUsuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia 'login' por la ruta a tu página de inicio de sesión
    else:
        form = RegistroForm()
    return render(request, 'Usuario/registrar.html', {'form': form})
