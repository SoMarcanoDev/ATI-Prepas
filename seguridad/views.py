from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class LoginView(auth_views.LoginView):
    template_name = 'login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'

@login_required(login_url='login')
def vista_protegida(request):
    return render(request, 'protegida.html')

def hello_world(request):
    return HttpResponse("¡Hola Mundo desde Django!")

def hola_mundo(request):
    return render(request, 'index.html')
