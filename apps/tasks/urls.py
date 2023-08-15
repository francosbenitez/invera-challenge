from django.urls import path

from .views import (
    TaskCreateAPIView,
    TaskDestroyAPIView,
    TaskListAPIView,
    TaskUpdateAPIView,
)

urlpatterns = [
    path("", TaskListAPIView.as_view(), name="task-list"),
    path("create/", TaskCreateAPIView.as_view(), name="task-create"),
    path("<int:pk>/", TaskUpdateAPIView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDestroyAPIView.as_view(), name="task-delete"),
]
