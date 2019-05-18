from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django.conf import settings
from .forms import RegisterForm

# Create your views here.
def login(request):
    return render(request, 'login.html')

def dashboard(request):
    template_name = 'user/dashboard.html'
    return render(request, template_name)

def registerUser(request):
    template_name = 'reg.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request, template_name, context)