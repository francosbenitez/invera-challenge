from logging import getLogger

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tasks.models import Task
from utils.mixins import TaskMixin

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
        if not request.data.get("task_id"):
            logger.error("No task id provided.")
            return Response(
                {"detail": "No task id provided.", "code": "no_task_id_provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task_ids = request.data.getlist("task_id")

        for task_id in task_ids:
            try:
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist:
                logger.error(f"Task with id {task_id} does not exist.")
                return Response(
                    {"detail": "Task does not exist.", "code": "task_does_not_exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if task in request.user.tasks.all():
                logger.error(f"Task with id {task_id} is already assigned to the user.")
                return Response(
                    {
                        "detail": "Task is already assigned to the user.",
                        "code": "task_already_assigned_to_user",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            request.user.tasks.add(task)

        logger.info(f"Tasks with ids {task_ids} have been assigned to the user.")
        return Response(
            {
                "detail": "Tasks assigned successfully.",
                "code": "tasks_assigned_successfully",
            },
            status=status.HTTP_200_OK,
        )


class UserTaskRemovalAPIView(APIView):
    """
    Allows users to remove assigned tasks.
    """

    def delete(self, request):
        if not request.data.get("task_id"):
            logger.error("No task id provided.")
            return Response(
                {"detail": "No task id provided.", "code": "no_task_id_provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task_ids = request.data.getlist("task_id")

        if not task_ids:
            logger.error("No task ids provided.")
            return Response(
                {"detail": "No task ids provided.", "code": "no_task_ids_provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for task_id in task_ids:
            try:
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist:
                logger.error(f"Task with id {task_id} does not exist.")
                return Response(
                    {"detail": "Task does not exist.", "code": "task_does_not_exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if task not in request.user.tasks.all():
                logger.error(f"Task with id {task_id} is not assigned to the user.")
                return Response(
                    {
                        "detail": "Task is not assigned to the user.",
                        "code": "task_not_assigned_to_user",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            request.user.tasks.remove(task)

        logger.info(f"Task with ids {task_ids} have been removed from the user.")
        return Response(
            {
                "detail": "Tasks removed successfully.",
                "code": "tasks_removed_successfully",
            },
            status=status.HTTP_200_OK,
        )
