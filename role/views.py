from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from role.forms import RoleForm
from role.models import Role

# Create your views here.
@login_required
def user_interests(request):
    return render (request, 'interests.html')

@login_required
def user_options(request):
    return render (request, 'options.html')

@login_required
def user_roles(request):
    form = RoleForm(request.POST or None)
    msg = ''
    if form.is_valid():
        form.save()
        form = RoleForm()
        msg = 'Cadastro realizado com sucesso!'
    
    context = {
        'form':form,
        'msg':msg,
    }
    return render(request, "roles.html", context)