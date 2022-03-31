import random


import pokemon as pokemon
from django.db.models import Model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from pokemons.models import Pokemon
from pokemons.api.permissions import IsAdminOrReadOnly
from pokemons.api.serializers import PokemonSerializer



class PokemonApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

class PokemonRandomView(APIView):
    def get(self, request):
        pokemons = Pokemon.objects.all()
        ids= [e.id for e in pokemons]
        id_aleatorio = random.choice(ids)
        pokemon_aleatorio = Pokemon.objects.get(id=id_aleatorio)
        serializer = PokemonSerializer(pokemon_aleatorio)
        return Response(serializer.data)

class ExpGanadaView(APIView):
    serializer_class = PokemonSerializer
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
                exp = serializer.validated_data.get('exp')
                print(exp)
                message = f'experiencia {exp}'
                # serializer.save()
                return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




