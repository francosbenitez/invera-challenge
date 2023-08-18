import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIClient

from apps.accounts.tests.factories import UserFactory
from apps.tasks.models import Task

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
def authenticated_api_client(api_client, user):
    """
    Returns an authenticated APIClient instance.
    """

    api_client.force_authenticate(user=user)

    return api_client


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

@pytest.fixture
def task_data():
    """
    Returns a dictionary of sample task data.
    """
  
    return {
        "title": "Test Task",
        "description": "This is a test task.",
    }

@pytest.fixture
def create_user(db, user_data):
    """ 
    Returns a sample user.
    """
  
    return User.objects.create_user(**user_data)

@pytest.fixture
def create_task(db, task_data):
    """ 
    Returns a sample task.
    """
  
    return Task.objects.create(**task_data)
  