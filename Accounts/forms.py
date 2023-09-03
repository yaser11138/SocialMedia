from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class MyUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")
        field_classes = {"username": UsernameField}


class MyUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "photo")
