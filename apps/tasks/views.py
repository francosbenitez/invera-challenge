from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


class TaskMixin:
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


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
        completed = self.request.query_params.get("completed")
        keyword = self.request.query_params.get("keyword")

        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(description__icontains=keyword)
            )

        if completed in ("true", "false"):
            queryset = queryset.filter(completed=(completed == "true"))

        sorted_queryset = queryset.order_by("-created_at")

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
