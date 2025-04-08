from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Profile


class UserCreationForm(UserCreationForm):
    """
    For Creating New User
    """

    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(UserChangeForm):
    """
    If you want to add something in future
    """

    class Meta:
        model = User
        fields = ("email",)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "avatar",
            "first_name",
            "last_name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
