from django.urls import include, path

from .views import (
    UserTaskAssignmentAPIView,
    UserTaskListAPIView,
    UserTaskRemovalAPIView,
)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path(
        "registration/",
        include("dj_rest_auth.registration.urls"),
    ),
    path("tasks/", UserTaskListAPIView.as_view(), name="user-task-list"),
    path(
        "tasks/assignment/",
        UserTaskAssignmentAPIView.as_view(),
        name="user-task-assignment",
    ),
    path("tasks/removal/", UserTaskRemovalAPIView.as_view(), name="user-task-removal"),
]
