from django.test import TestCase

from apps.tasks.models import Task


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
        )

    def test_task_defaults(self):
        self.assertEqual(self.task.completed, False)

    def test_task_creation(self):
        self.assertIsInstance(self.task, Task)

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), "Test Task")

    def test_task_updated_at(self):
        old_updated_at = self.task.updated_at
        self.task.title = "Updated Task Title"
        self.task.save()
        new_updated_at = Task.objects.get(pk=self.task.pk).updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
