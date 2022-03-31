from django.urls import path
from rest_framework.routers import DefaultRouter
from pokemons.api.views import PokemonApiViewSet
from pokemons.api.views import PokemonRandomView,ExpGanadaView

routerPokemon = DefaultRouter()
routerPokemon.register(prefix='pokemons',basename='pokemons', viewset=PokemonApiViewSet)

urlpatterns = [
    path('pokemonrandom', PokemonRandomView.as_view()),
    path('expvictoria', ExpGanadaView.as_view())
]