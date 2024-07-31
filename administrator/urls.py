from django.urls import path
from . import views

urlpatterns = [
    #Aqui iran las urls de administrador
    # path('index', views.index), Cuando termine agregar esta
    path('', views.admin, name="admin"),
]