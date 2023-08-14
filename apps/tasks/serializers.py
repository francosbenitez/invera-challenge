from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializes the Task model.
    """

    class Meta:
        model = Task
        fields = "__all__"
