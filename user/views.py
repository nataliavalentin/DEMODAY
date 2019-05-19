from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from user.forms import UserForm
from user.models import User
from django.conf import settings
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'login.html')

@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)
    
def register(request):
    formulario = UserForm(request.POST or None)
    msg = ''
    if formulario.is_valid():
        formulario.save()
        formulario = UserForm()
        msg = 'Cadastro realizado com sucesso!'
    
    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'register.html', contexto)

def registerUser(request):
    template_name = 'reg.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username = user.username, password=form.cleaned_data['password1'])
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request, template_name, context)