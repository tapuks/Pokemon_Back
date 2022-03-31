from django.contrib import admin
from pokemons.models import Pokemon

@admin.register(Pokemon)
class PokemonsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level']
