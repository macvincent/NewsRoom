from django.urls import path
from authentication.views import CreateUser

urlpatterns = [
    path('', CreateUser.as_view())
]
