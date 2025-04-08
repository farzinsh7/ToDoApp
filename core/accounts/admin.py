from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = (
        "email",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
        ("Group Permissions", {"fields": ("groups", "user_permissions")}),
        ("User Logs", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            "Authentication",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name")
    searching_fields = ("user", "first_name", "last_name")


admin.site.register(User, CustomUserAdmin)
