from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from task.models import TaskModel
from staff.models import StaffModel


class TaskAPIView(APIView):
    """ Класс для получения и создания задач """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task/tasks.html'

    def get(self, request: Request) -> Response:
        try:
            tasks = TaskModel.objects.prefetch_related('subcategories').filter(parent=None)

            staff_list = StaffModel.objects.all()  # Получаем всех исполнителей

            return Response({'tasks': tasks, 'staff_list': staff_list})
        except Exception as e:
            return Response(f"Ошибка: {e}", status=500)

    def post(self, request: Request) -> Response:
        data = request.data
        print(data)
        title = data.get("title")
        executor_id = data.get("executor")
        period = data.get("period")
        parent_id = data.get("parent")
        status = data.get("status")

        if executor_id:
            executor = get_object_or_404(StaffModel, id=executor_id)
        else:
            executor = None
        parent_task = TaskModel.objects.get(id=parent_id) if parent_id else None

        TaskModel.objects.create(
            title=title,
            executor=executor,
            period=period,
            parent=parent_task,
            status=status
        )
        return redirect('tasks')


class TaskDeleteAPIView(APIView):
    """ Класс для удаления задач """

    def post(self, request, pk):
        task = get_object_or_404(TaskModel, id=pk)
        task.delete()
        return redirect('tasks')


class TaskUpdateAPIView(APIView):
    """ Класс для редактирования задач """

    def get(self, request, pk):
        task = get_object_or_404(TaskModel, id=pk)
        tasks = TaskModel.objects.prefetch_related('subcategories').filter(parent=None)
        staff_list = StaffModel.objects.all()
        return render(request, 'task/task-update.html', {'task': task, "staff_list": staff_list, "tasks": tasks})

    def post(self, request: Request, pk: int) -> Response:
        task = get_object_or_404(TaskModel, id=pk)

        title = request.POST.get("title")
        executor_id = request.POST.get("executor")
        period = request.POST.get("period")
        status = request.POST.get("status")

        if title:
            task.title = title
        if executor_id:
            task.executor_id = executor_id
        if period:
            task.period = period
        if status:
            task.status = status

        task.save()

        return redirect("tasks")
