from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Nome', max_length=255)
    last_name = forms.CharField(label='Sobrenome', max_length=255)
    email = forms.EmailField(label='E-mail')
    cellphone = forms.CharField(label='Telefone', max_length=11)
    birthday = forms.DateField(label='Data de Nascimento')

    #Sobrescrever metodo Save do form
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.cellphone = self.cleaned_data['cellphone']
        user.birthday = self.cleaned_data['birthday']
        if commit:
            user.save()
        return user



