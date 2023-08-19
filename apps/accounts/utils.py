from logging import getLogger

from rest_framework import status
from rest_framework.response import Response

from apps.tasks.models import Task

logger = getLogger(__name__)


def handle_task_action(request, action):
    """
    Handles task assignment and removal.
    """

    word = "assigned" if action == "assignment" else "removed"

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

        if action == "removal":
            if task not in request.user.tasks.all():
                logger.error(f"Task with id {task_id} is not {word} to the user.")

                return Response(
                    {
                        "detail": f"Task is not {word} to the user.",
                        "code": f"task_not_{word}_to_user",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            request.user.tasks.remove(task)
        elif action == "assignment":
            if task in request.user.tasks.all():
                logger.error(f"Task with id {task_id} is already {word} to the user.")

                return Response(
                    {
                        "detail": f"Task is already {word} to the user.",
                        "code": f"task_already_{word}_to_user",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            request.user.tasks.add(task)

    logger.info(f"Task with ids {task_ids} have been {word} from the user.")

    return Response(
        {
            "detail": f"Tasks {word} successfully.",
            "code": f"tasks_{word}_successfully",
        },
        status=status.HTTP_200_OK,
    )
