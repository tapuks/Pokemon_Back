from rest_framework import serializers
from pokemons.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id','name','level', 'exp']
#
# class ExpGanadaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pokemon
#         fields = ['id','exp']