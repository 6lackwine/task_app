from datetime import datetime

from django.db import models

from staff.models import StaffModel


class TaskModel(models.Model):
    """ Класс для создания модели задачи """
    title = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="subcategories")
    executor = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    period = models.DateTimeField()
    status = models.CharField(max_length=100)
