# Generated by Django 2.2.1 on 2019-05-19 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establishment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipos_role', models.CharField(choices=[('Música', 'Música'), ('Fotografia', 'Fotografia'), ('Moda', 'Moda'), ('Bons Drinks', 'Bons Drinks'), ('Viagem', 'viagem'), ('Diversão', 'Diversão')], max_length=50)),
                ('data_role', models.DateField()),
                ('horario_role', models.TimeField()),
                ('local_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishment.Establishment')),
            ],
        ),
    ]
