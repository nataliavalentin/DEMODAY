from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_last_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_cellphone = models.CharField(max_length=11)
    user_birthday = models.DateField()

    def __str__(self):
        return self.user_name