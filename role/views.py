from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from role.forms import RoleForm, RoleGenreForm
from role.models import Role
from establishment.models import Establishment

# Create your views here.
@login_required
def user_interests(request):
    formulario = RoleGenreForm(request.POST or None)
    msg = ''
    if formulario.is_valid():
        formulario.save()
        formulario = RoleGenreForm()
        msg = 'Cadastro realizado com sucesso!'
    
    contexto = {
        'form' : formulario,
        'msg' : msg,
    }
    return render(request, 'interests.html', contexto)

@login_required
def user_options(request):
    lista = Establishment.objects.all()
    context = {'lista': lista}
    return render (request, 'options.html', context)

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
