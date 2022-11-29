from django.db import models

class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    cedula = models.CharField('Cedula', max_length=12, unique=True)
    correo = models.EmailField('Email', max_length=100, unique=True)
    celular = models.CharField('Celular', max_length=10, unique=True)
    direccion = models.CharField('Direccion', max_length=100)
    cargo = models.CharField('Cargo', max_length=30)
    contrasena = models.CharField('Contrasena', max_length=15, unique=True)