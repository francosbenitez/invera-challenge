from logging import getLogger

from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.accounts.tests.factories import UserFactory
from apps.tasks.models import Task

logger = getLogger(__name__)


User = get_user_model()


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="testpassword",
            first_name="John",
            last_name="Doe",
        )
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
        )
        self.user.tasks.add(self.task)

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), "test@example.com")

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), "John Doe")

    def test_default_permissions(self):
        self.assertFalse(self.user.is_admin)
        self.assertFalse(self.user.is_staff)

    def test_assigned_tasks(self):
        self.assertEqual(self.user.tasks.count(), 1)
        self.assertEqual(self.user.tasks.first(), self.task)

    def test_user_model_with_factory(self):
        UserFactory()
        self.assertEqual(User.objects.count(), 2)
