from django.urls import path
from . import views

urlpatterns = [
    #Aqui iran las urls de administrador
    path('', views.enviar, name="admin"),
    path('logout', views.logoutview, name="logout"),
    path('enviar', views.enviar, name='enviar'),
    path('obtener_libro/<int:libro_id>/', views.obtener_libro, name='obtener_libro'),
    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
]