from django.urls import path

from .views import (
    TaskCreateAPIView,
    TaskDestroyAPIView,
    TaskListAPIView,
    TaskUpdateAPIView,
)

urlpatterns = [
    path("tasks/", TaskListAPIView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateAPIView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskUpdateAPIView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDestroyAPIView.as_view(), name="task-delete"),
]
