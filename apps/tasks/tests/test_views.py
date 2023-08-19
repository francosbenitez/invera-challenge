from datetime import datetime
from logging import getLogger

import pytest
from django.urls import reverse
from rest_framework import status

from apps.tasks.models import Task

logger = getLogger(__name__)


@pytest.mark.django_db
def test_list_tasks_by_authenticated_user(authenticated_api_client):
    url = reverse("task-list")
    response = authenticated_api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_list_tasks_by_unauthenticated_user(api_client):
    url = reverse("task-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_filter_tasks_by_content(authenticated_api_client, task):
    url = reverse("task-list")
    response = authenticated_api_client.get(url, query_params={"content": "Task"})
    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"][0]["title"] == task.title


@pytest.mark.django_db
def test_filter_tasks_by_date(authenticated_api_client, task):
    url = reverse("task-list")
    response = authenticated_api_client.get(
        url, query_params={"date": datetime.now().strftime("%Y-%m-%d")}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"][0]["title"] == task.title


@pytest.mark.django_db
def test_create_task(authenticated_api_client, task_data):
    url = reverse("task-create")
    response = authenticated_api_client.post(url, data=task_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1


@pytest.mark.django_db
def test_update_task(authenticated_api_client, task, task_update_data):
    url = reverse("task-update", kwargs={"pk": task.id})
    response = authenticated_api_client.patch(url, data=task_update_data)
    assert response.status_code == status.HTTP_200_OK
    task.refresh_from_db()
    assert task.title == task_update_data["title"]
    assert task.completed == task_update_data["completed"]


@pytest.mark.django_db
def test_delete_task(authenticated_api_client, task):
    url = reverse("task-delete", kwargs={"pk": task.id})
    response = authenticated_api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Task.objects.count() == 0
