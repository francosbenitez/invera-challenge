from logging import getLogger

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.tests.factories import UserFactory
from apps.tasks.models import Task

User = get_user_model()

logger = getLogger(__name__)


class TaskViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            "title": "Sample Task",
            "description": "This is a sample task.",
            "completed": False,
        }
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(**self.task_data)
        self.task_update_data = {"title": "Updated Task", "completed": True}

        # logger.info("self.task.id from setUp: %s", self.task.id)

    def test_create_task(self):
        url = reverse("task-create")
        response = self.client.post(url, data=self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_list_tasks(self):
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        url = reverse("task-update", kwargs={"pk": self.task.id})
        response = self.client.patch(url, data=self.task_update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")
        self.assertEqual(self.task.completed, True)

    def test_delete_task(self):
        url = reverse("task-delete", kwargs={"pk": self.task.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
