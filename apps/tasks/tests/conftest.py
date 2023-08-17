import pytest
from rest_framework.test import APIClient

from apps.tasks.models import Task


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def task():
    task = Task.objects.create(
        title="Title 1",
        description="Description 1",
        completed=False,
    )

    return task
