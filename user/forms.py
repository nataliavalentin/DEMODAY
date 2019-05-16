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