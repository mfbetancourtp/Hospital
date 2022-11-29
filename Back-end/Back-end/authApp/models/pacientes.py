from django.db import models
from .empleados import Empleados
from .user import User

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length = 50)
    apellidos = models.CharField('Apellidos', max_length = 50)
    tipo_de_identificacion = models.CharField('tipo de identificacion', max_length = 50)
    nro_identificacion  = models.CharField('Numero de identificacion', max_length = 50, unique=True)
    email = models.EmailField('Email', max_length = 50, unique=True)
    celular  = models.CharField('celular', max_length = 50, unique=True)
    id_usuario  = models.ForeignKey(User, on_delete=models.CASCADE)
    id_empleado  = models.ForeignKey(Empleados, on_delete=models.CASCADE)
   