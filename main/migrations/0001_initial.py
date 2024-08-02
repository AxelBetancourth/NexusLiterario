# Generated by Django 5.0.7 on 2024-08-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('Id_User', models.AutoField(db_column='Id_User', primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('cliente', 'Cliente'), ('administrador', 'Administrador')], default='cliente', max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]