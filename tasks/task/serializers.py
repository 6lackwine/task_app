from rest_framework import serializers

from task.models import TaskModel


class TaskSerializers(serializers.ModelSerializer):
    """ Класс для сериализации задач """
    class Meta:
        model = TaskModel
        fields = "id", "title", "executor", "period", "status"