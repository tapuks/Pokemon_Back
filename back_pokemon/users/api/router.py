from django.urls import path
from users.api.views import RegisterView, UserView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

# from users.api.views import HelloApiView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/me', UserView.as_view()),

    # path('hello-view/', HelloApiView.as_view())
]