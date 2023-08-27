from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have Username')

        if not password:
            raise ValueError('User must have an password')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """ Create a new superuser profile """
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class MyUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True)
    objects = MyUserManager()
    email = models.EmailField(unique=True, validators=[EmailValidator],)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]
