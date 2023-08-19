from rest_framework.permissions import IsAuthenticated

from apps.tasks.serializers import TaskSerializer


class TaskMixin:
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
