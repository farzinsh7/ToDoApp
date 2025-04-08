from django.urls import path, include
from . import views


app_name = "accounts"
urlpatterns = [
    # API
    path("api/v1/", include("accounts.api.v1.urls")),
    # Other EndPoints
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile-edit/", views.ProfileEditView.as_view(), name="profile-edit"),
]
