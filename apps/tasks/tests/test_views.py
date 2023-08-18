from logging import getLogger

import pytest
from django.urls import reverse
from rest_framework import status

from apps.tasks.models import Task

logger = getLogger(__name__)


@pytest.mark.django_db
def test_create_task(authenticated_api_client, task_data):
    url = reverse("task-create")
    response = authenticated_api_client.post(url, data=task_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1


@pytest.mark.django_db
def test_list_tasks(authenticated_api_client):
    url = reverse("task-list")
    response = authenticated_api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_task(authenticated_api_client, task, task_update_data):
    url = reverse("task-update", kwargs={"pk": task.id})
    response = authenticated_api_client.patch(url, data=task_update_data)
    assert response.status_code == status.HTTP_200_OK
    task.refresh_from_db()
    assert task.title == "Updated Task"
    assert task.completed


@pytest.mark.django_db
def test_delete_task(authenticated_api_client, task):
    url = reverse("task-delete", kwargs={"pk": task.id})
    response = authenticated_api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Task.objects.count() == 0
