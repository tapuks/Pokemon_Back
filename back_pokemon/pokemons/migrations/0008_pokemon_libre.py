# Generated by Django 4.0.3 on 2022-03-31 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0007_alter_pokemon_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='libre',
            field=models.BooleanField(default=True),
        ),
    ]
