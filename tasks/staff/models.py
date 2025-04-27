from django.contrib.auth.models import User
from django.db import models


class StaffModel(models.Model):
    """ Класс для создания модели пользователей """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="users", verbose_name="Пользователь")
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
