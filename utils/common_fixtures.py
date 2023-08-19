import pytest
from rest_framework.test import APIClient

from apps.accounts.tests.factories import UserFactory
from apps.tasks.models import Task


@pytest.fixture
def api_client():
    """
    Returns an APIClient instance.
    """

    return APIClient()


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
def task_data():
    """
    Returns a dictionary of sample task data.
    """

    return {
        "title": "Sample Task",
        "description": "This is a sample task.",
        "completed": False,
    }


@pytest.fixture
def task(user, task_data):
    """
    Returns a sample task.
    """

    return Task.objects.create(user=user, **task_data)
