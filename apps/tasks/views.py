from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
)

from utils.mixins import TaskMixin

from .models import Task


class TaskCreateAPIView(TaskMixin, CreateAPIView):
    """
    Creates a new task.
    """


class TaskListAPIView(TaskMixin, ListAPIView):
    """
    Lists all tasks.
    """

    def get_queryset(self):
        queryset = Task.objects.all()
        content = self.request.query_params.get("content")
        created_at = self.request.query_params.get("created_at")

        if created_at:
            queryset = queryset.filter(created_at__icontains=created_at)

        if content:
            queryset = queryset.filter(
                Q(title__icontains=content) | Q(description__icontains=content)
            )

        sorted_queryset = queryset.order_by("id")

        return sorted_queryset


class TaskDestroyAPIView(TaskMixin, DestroyAPIView):
    """
    Deletes a task.
    """

    queryset = Task.objects.all()


class TaskUpdateAPIView(TaskMixin, UpdateAPIView):
    """
    Updates a task.
    """

    queryset = Task.objects.all()
