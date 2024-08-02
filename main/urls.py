from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('auth/register', views.user, name="user"),
    path('auth/login', views.login, name="login"),
]

