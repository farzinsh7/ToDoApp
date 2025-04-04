from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from . import views


urlpatterns = [
    # Registration
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    
    # Authontication by auth-token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="toke-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    
    # Authontication by jwt
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),

]
