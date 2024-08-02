from django.db import models
import os

# Create your models here.

class Users(models.Model):
    
    CLIENTE = 'cliente'
    ADMINISTRADOR = 'administrador'
    
    TIPO_CHOICES = [
        (CLIENTE, 'Cliente'),
        (ADMINISTRADOR, 'Administrador'),
    ]
    
    Id_User = models.AutoField(primary_key=True, db_column='Id_User')
    correo = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, default=CLIENTE)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user_name
        
    class Meta:
        db_table = 'Users'
