from django.urls import path

from .views import TaskAPIView, TaskDeleteAPIView, TaskUpdateAPIView

urlpatterns = [
    path("tasks/", TaskAPIView.as_view(), name="tasks"),
    path('tasks/create/', TaskAPIView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='task-delete'),
]
