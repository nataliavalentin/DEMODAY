from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ["local_role", "tipos_role", "data_role", "horario_role"]

    def __init__(self, *args, **kwargs):
        super(RoleForm, self).__init__(*args, **kwargs)
        self.fields['local_role'].label = "Local"
        self.fields['tipos_role'].label = "Tipo"
        self.fields['data_role'].label = "Data"
        self.fields['horario_role'].label = "Horário"