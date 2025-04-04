from django.urls import path
from . import views


urlpatterns = [
    # Authontication by auth-token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="toke-login"),

]
