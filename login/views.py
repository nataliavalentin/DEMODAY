from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def Login(request):
    return render(request, 'login.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta!")
    return redirect("home:index")