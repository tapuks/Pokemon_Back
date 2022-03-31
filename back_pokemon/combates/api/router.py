from django.urls import path
from rest_framework.routers import DefaultRouter
from combates.api.views import CombatesApiViewSet



urlpatterns = [
    path('exp-combate', ExpGanadaView.as_view())
]