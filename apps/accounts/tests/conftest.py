import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIClient

from apps.accounts.tests.factories import UserFactory

User = get_user_model()


@pytest.fixture
def api_client():
    """
    Returns an APIClient instance.
    """

    return APIClient()


@pytest.fixture
def registration_url():
    return "/api/accounts/registration/"


@pytest.fixture
def login_url():
    return "/api/accounts/login/"


@pytest.fixture
def user():
    """
    Returns a sample user.
    """

    return UserFactory()


@pytest.fixture
def user_data():
    """
    Returns a dictionary of sample user data.
    """

    return {
        "first_name": "Franco",
        "last_name": "Benitez",
        "email": "francosbenitez@gmail.com",
        "password1": "holaquetal",
        "password2": "holaquetal",
    }


@pytest.fixture
def invalid_user():
    """
    Returns a dictionary of invalid user data.
    """

    return {
        "email": "nonexistentuser@email.com",
        "password": "nonexistentuser",
    }


@pytest.fixture
def valid_user():
    """
    Returns a dictionary of valid user data.
    """

    return User.objects.create_user(
        password="holaquetal",
        last_login=timezone.now(),
        is_admin=False,
        email="francosbenitez@gmail.com",
        first_name="Franco",
        is_active=True,
        is_staff=False,
        last_name="Benitez",
    )
