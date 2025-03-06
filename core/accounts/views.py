from django.shortcuts import render
from django.contrib.auth import views as auth_view
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm, ProfileEditForm
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


# Create your views here.
class LoginView(SuccessMessageMixin, auth_view.LoginView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    success_message = "Welcome Back"


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_message = "Your Account Created Successfully"
    success_url = reverse_lazy("todo:index")


class LogoutView(auth_view.LogoutView):
    pass



class ProfileEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "accounts/profile-edit.html"
    form_class = ProfileEditForm
    success_url = reverse_lazy("accounts:profile-edit")
    success_message = "Your Profile Successfully Updated"

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)