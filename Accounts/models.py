from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


def user_directory_path(instance, filename):
    return '{0}/profile_photo/{1}'.format(instance.username, filename)


class MyUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(unique=True, validators=[EmailValidator])
    photo = models.ImageField(upload_to=user_directory_path, default="default-profile.png")
    is_active = models.BooleanField(
        default=False,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    bio = models.TextField(null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]
