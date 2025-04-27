from django.urls import path

from staff.views import SignUpAPIView, SignIn, SignOut

urlpatterns = [
    path("register/", SignUpAPIView.as_view(), name="register"),
    path("login/", SignIn.as_view(), name="login"),
    path("logout/", SignOut.as_view(), name="logout")
]
