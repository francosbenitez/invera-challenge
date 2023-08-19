from logging import getLogger

import pytest
from django.urls import reverse
from rest_framework import status

logger = getLogger(__name__)


@pytest.mark.django_db
def test_successful_user_registration(api_client, registration_url, user_data):
    response = api_client.post(registration_url, user_data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_successful_user_login(api_client, login_url, valid_user):
    response = api_client.post(
        login_url, {"email": valid_user.email, "password": "holaquetal"}
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_failed_login_with_invalid_credentials(api_client, login_url, invalid_user):
    response = api_client.post(login_url, invalid_user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "non_field_errors": ["Unable to log in with provided credentials."]
    }


@pytest.mark.django_db
def test_user_task_list(authenticated_api_client, assigned_task):
    url = reverse("user-task-list")
    response = authenticated_api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"][0]["title"] == assigned_task.title


@pytest.mark.django_db
def test_user_task_assignment(authenticated_api_client, task):
    url = reverse("user-task-assignment")
    data = {"task_id": task.id}
    response = authenticated_api_client.post(url, data=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "detail": "Tasks assigned successfully.",
        "code": "tasks_assigned_successfully",
    }


@pytest.mark.django_db
def test_user_task_removal(authenticated_api_client, assigned_task):
    url = reverse("user-task-removal")
    data = {"task_id": assigned_task.id}
    response = authenticated_api_client.delete(url, data=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "detail": "Tasks removed successfully.",
        "code": "tasks_removed_successfully",
    }
