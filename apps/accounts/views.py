from logging import getLogger

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from utils.mixins import TaskMixin

from .utils import handle_task_action

logger = getLogger(__name__)


class UserTaskListAPIView(TaskMixin, ListAPIView):
    """
    Lists all tasks of the current user.
    """

    def get_queryset(self):
        return self.request.user.tasks.all().order_by("id")


class UserTaskAssignmentAPIView(TaskMixin, APIView):
    """
    Allows users to assign tasks to themselves.
    """

    def post(self, request):
        return handle_task_action(request, "assignment")


class UserTaskRemovalAPIView(APIView):
    """
    Allows users to remove assigned tasks.
    """

    def delete(self, request):
        return handle_task_action(request, "removal")
