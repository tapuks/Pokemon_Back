# Generated by Django 4.0.3 on 2022-03-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='exp_derrota',
            field=models.IntegerField(),
        ),
    ]