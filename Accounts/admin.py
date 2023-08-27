from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm
from .models import MyUser


class MyUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = MyUser
        fields = ("email", "username")


class MyUserChangeFrom(UserChangeForm):
    class Meta:
        model = MyUser
        fields = "__all__"


@admin.register(MyUser)
class UserAmin(BaseUserAdmin):
    form = MyUserChangeFrom
    add_form = MyUserCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("username","first_name", "last_name", "phone_number")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
