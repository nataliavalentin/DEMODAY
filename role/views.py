from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_interests(request):
    return render (request, 'interests.html')

@login_required
def user_options(request):
    return render (request, 'options.html')
