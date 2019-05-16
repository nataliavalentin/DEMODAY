from django.shortcuts import render

# Create your views here.

def user_interests(request):
    return render (request, 'interests.html')

def user_options(request):
    return render (request, 'options.html')
