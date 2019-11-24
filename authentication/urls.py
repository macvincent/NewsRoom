from django.urls import path
from authentication.views import CreateUser
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signUp', CreateUser.as_view(), name = "signUp"),
    path('', LoginView.as_view(), name = "login"),
]
