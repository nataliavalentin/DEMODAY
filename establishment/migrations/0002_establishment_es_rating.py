# Generated by Django 2.2 on 2019-05-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='es_rating',
            field=models.IntegerField(null=True),
        ),
    ]