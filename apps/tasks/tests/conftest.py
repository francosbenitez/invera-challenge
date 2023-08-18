import pytest

from apps.tasks.models import Task
from utils.common_fixtures import api_client, authenticated_api_client, user


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
def task_update_data():
    """
    Returns a dictionary of sample task update data.
    """

    return {
        "title": "Updated Task",
        "completed": True,
    }


@pytest.fixture
def task(user, task_data):
    """
    Returns a sample task.
    """

    return Task.objects.create(user=user, **task_data)
