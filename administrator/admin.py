from django.contrib import admin
#Importar mis modelos
from .models import Libros, Categorias, Categorias_Libros

# Register your models here.
admin.site.register(Libros)
admin.site.register(Categorias)
admin.site.register(Categorias_Libros)
