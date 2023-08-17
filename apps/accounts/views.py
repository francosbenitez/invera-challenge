from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


class TaskMixin:
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class UserTaskListAPIView(TaskMixin, ListAPIView):
    """
    Lists all tasks of the current user.
    """

    def get_queryset(self):
        return self.request.user.tasks.all()


class UserTaskAssignmentAPIView(TaskMixin, APIView):
    """
    Allows users to assign tasks to themselves.
    """

    def post(self, request):
        task_id = request.data.get("task_id")
        task = get_object_or_404(Task, id=task_id)
        request.user.tasks.add(task)

        return Response(status=status.HTTP_200_OK)


class UserTaskRemovalAPIView(APIView):
    """
    Allows users to remove assigned tasks.
    """

    def delete(self, request):
        task_id = request.data.get("task_id")
        task = get_object_or_404(Task, id=task_id)
        request.user.tasks.remove(task)

        return Response(status=status.HTTP_200_OK)
