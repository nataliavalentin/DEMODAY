from django import forms
from user.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =[
            'user_name',
            'user_last_name',
            'user_email',
            'user_cellphone',
            'user_birthday'
        ]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].label = "Nome"
        self.fields['user_last_name'].label = "Sobrenome"
        self.fields['user_email'].label = "E-mail"
        self.fields['user_cellphone'].label = "Celular"
        self.fields['user_birthday'].label = "Data de Nascimento"