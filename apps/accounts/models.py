from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

from .managers import UserManager


class User(AbstractBaseUser):
    """
    Custom User model representing a user of the application.
    """

    # User fields
    email = models.EmailField(
        unique=True, error_messages={"unique": "Este email ya está registrado."}
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    # Configuration
    USERNAME_FIELD = "email"  # Field used for authentication
    REQUIRED_FIELDS = []  # Other required fields for user creation

    objects = UserManager()  # Custom manager for user operations

    # Methods
    def get_full_name(self):
        """
        Returns the full name of the user.
        """

        return self.first_name + " " + self.last_name
