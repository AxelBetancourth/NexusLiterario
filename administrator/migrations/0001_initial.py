# Generated by Django 5.0.7 on 2024-07-30 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('Id_Categorias', models.AutoField(db_column='Id_Categorias', primary_key=True, serialize=False)),
                ('Categorias', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('Id_Libros', models.AutoField(db_column='Id_Libros', primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=50)),
                ('Autor', models.CharField(max_length=30)),
                ('Precio', models.IntegerField()),
                ('Descripcion', models.TextField()),
                ('Fecha_Publicacion', models.DateField()),
                ('Fecha_Now', models.DateField(auto_now_add=True)),
                ('Img_Portada', models.ImageField(null=True, upload_to='portadas')),
            ],
            options={
                'db_table': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='Categorias_Libros',
            fields=[
                ('Id_Categorias_Libros', models.AutoField(db_column='Id_Categorias_Libros', primary_key=True, serialize=False)),
                ('Id_Categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.categorias')),
                ('Id_Libros', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.libros')),
            ],
            options={
                'db_table': 'Categorias_Libros',
            },
        ),
    ]
