from django.urls import path
from . import views


urlpatterns = [
    # Registration
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    
    # Authontication by auth-token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="toke-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),

]
