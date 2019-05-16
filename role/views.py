from django.shortcuts import render

# Create your views here.

def user_interests(request):
    return render (request, 'interests.html')
