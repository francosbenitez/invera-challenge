import pytest

from apps.tasks.models import Task
from utils.common_fixtures import (
    api_client,
    authenticated_api_client,
    task,
    task_data,
    user,
)


@pytest.fixture
def task_update_data():
    """
    Returns a dictionary of sample task update data.
    """

    return {
        "title": "Updated Task",
        "completed": True,
    }
