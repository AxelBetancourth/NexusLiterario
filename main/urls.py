from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.main, name="main"),
    path('', views.main2, name="inicio"),
    path('auth/register', views.user, name="user"),
    path('auth/login', views.login, name="login"),
]

