
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from pokemons.api.router import routerPokemon

schema_view = get_schema_view(
    openapi.Info(
        title="Pokemon API",
        default_version='v1',
        description="Documentacion de la API de pokemons de David",
        terms_of_service="",  # TO DO URL DE TERMINOS Y CONDICIONES
        contact=openapi.Contact(email="david_berdiell@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include('pokemons.api.router')),
    path('api/', include(routerPokemon.urls)),
]
