from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

class LoginView(auth_views.LoginView):
    template_name = 'login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'

@login_required(login_url='login')
def vista_protegida(request):
    return render(request, 'protegida.html')
