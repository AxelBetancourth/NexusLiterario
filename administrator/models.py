from django.db import models
import os

# Create your models here.

class Libros(models.Model):
    Id_Libros = models.AutoField(primary_key=True, db_column='Id_Libros')
    Titulo = models.CharField(max_length=50)
    Autor = models.CharField(max_length=30)
    Precio = models.IntegerField()
    Descripcion = models.TextField()
    Fecha_Publicacion = models.DateField()
    Fecha_Now = models.DateTimeField(auto_now_add=True)
    Img_Portada = models.ImageField(upload_to='portadas' , null=True)
    
    def __str__(self):
        return self.Titulo
    
    def delete(self, *args, **kwargs):
        if self.Img_Portada:
            if os.path.isfile(self.Img_Portada.path):
                os.remove(self.Img_Portada.path)
        super().delete(*args, **kwargs)
        
    class Meta:
        db_table = 'Libros'
        
class Categorias(models.Model):
    Id_Categorias = models.AutoField(primary_key=True, db_column='Id_Categorias')
    Categorias = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Categorias
    
    class Meta:
        db_table = 'Categorias'
        
class Categorias_Libros(models.Model):
    Id_Categorias_Libros = models.AutoField(primary_key=True, db_column='Id_Categorias_Libros')
    Id_Libros = models.ForeignKey(Libros, on_delete=models.CASCADE)
    Id_Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Id_Libros.Titulo} - {self.Id_Categorias.Categorias}"
    
    class Meta:
        db_table = 'Categorias_Libros'
        

#python manage.py makemigrations
#python manage.py migrate
