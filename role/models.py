from django.db import models
from establishment.models import Establishment
from multiselectfield import MultiSelectField
# Create your models here.
class Role(models.Model):
    opcoes_role = [
        ('Música', 'Música'),
        ('Fotografia', 'Fotografia'),
        ('Moda', 'Moda'),
        ('Bons Drinks', 'Bons Drinks'),
        ('Viagem', 'viagem'),
        ('Diversão', 'Diversão'),        
    ]
    local_role = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    tipos_role = models.CharField(max_length=50, choices=opcoes_role)
    data_role = models.DateField()
    horario_role = models.TimeField(auto_now = False, auto_now_add = False)

class TiposRole(models.Model):
    role_genres = [
        ('1', 'Tecnologia'),
        ('2', 'Diversão'),
        ('3', 'Fotografia'),
        ('4', 'Gastronomia'),
        ('5', 'Bons Drinks'),
        ('6', 'Música'),
        ('7', 'Moda'),
        ('8', 'Viagem')
    ]
    choices = MultiSelectField(choices=role_genres)