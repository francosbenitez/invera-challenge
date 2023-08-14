from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the User model, providing helper methods for user creation.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.

        :param email: The email address of the user.
        :param password: The password for the user.
        :param extra_fields: Additional fields to be saved in the user model.
        :return: The created user instance.
        """

        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.

        :param email: The email address of the superuser.
        :param password: The password for the superuser.
        :return: The created superuser instance.
        """

        if password is None:
            raise TypeError("Superusers must have a password")

        user = self.model(email=email)
        user.is_admin = True
        user.is_staff = True
        user.set_password(password)
        user.save()

        return user
