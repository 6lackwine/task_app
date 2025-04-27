from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from staff.models import StaffModel


class SignUpAPIView(APIView):
    """ Класс для регистрации пользователя """
    def get(self, request: Request) -> Response:
        """ Отображение страницы регистрации """
        return render(request, "staff/register.html")
    """ Класс для регистрации пользователя """
    def post(self, request: Request) -> Response:
        """ Функция регистрирует пользователя, аутентифицирует и авторизирует его """
        user_data = request.data
        first_name = user_data.get("first_name")
        username = user_data.get("username")
        password = user_data.get("password")
        last_name = user_data.get("last_name")
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user = authenticate(request, username=username, password=password)
        StaffModel.objects.create(user=user, firstname=first_name, surname=last_name)
        if user is not None:
            login(request, user)
            return render(request, "staff/register.html", {})
            #return Response(status=200)
        else:
            return Response({"error": "Authentication failed."}, status=401)


class SignOut(APIView):
    """ Класс для деавторизации """
    def get(self, request: Request) -> Response:
        return render(request, "staff/login.html")
    def post(self, request: Request) -> Response:
        logout(request)
        return reverse_lazy('staff:login')


class SignIn(APIView):
    """ Класс для аутентификации и авторизации пользователя """
    def get(self, request: Request) -> Response:
        return render(request, "staff/login.html")

    def post(self, request: Request) -> Response:
        user_data = request.data
        username = user_data["username"]
        password = user_data["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return render(request, "staff/login.html", {})
        else:
            # return render(request, "staff/login.html", {"error": "Authentication failed."})
            return Response({"error": "Authentication failed."}, status=401)