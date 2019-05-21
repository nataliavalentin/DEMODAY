from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=11)
    birthday = models.DateField(null=True)

    tecnologia = models.BooleanField(default=False)
    diversao = models.BooleanField(default=False)
    fotografia = models.BooleanField(default=False)
    gastronomia = models.BooleanField(default=False)
    bons_drinks = models.BooleanField(default=False)
    musica = models.BooleanField(default=False)
    moda = models.BooleanField(default=False)
    viagem = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ('Perfil')
        verbose_name_plural = ('Perfis')