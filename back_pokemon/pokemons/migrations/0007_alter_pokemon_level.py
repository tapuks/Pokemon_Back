# Generated by Django 4.0.3 on 2022-03-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0006_pokemon_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
