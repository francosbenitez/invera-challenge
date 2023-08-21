from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from django.urls import path

from .views import (
    UserTaskAssignmentAPIView,
    UserTaskListAPIView,
    UserTaskRemovalAPIView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="user-login"),
    path(
        "registration/",
        RegisterView.as_view(),
        name="user-register",
    ),
    path("tasks/", UserTaskListAPIView.as_view(), name="user-task-list"),
    path(
        "tasks/assignment/",
        UserTaskAssignmentAPIView.as_view(),
        name="user-task-assignment",
    ),
    path("tasks/removal/", UserTaskRemovalAPIView.as_view(), name="user-task-removal"),
]
