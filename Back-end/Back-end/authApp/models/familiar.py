from django.db import models
from .pacientes import Pacientes

class Familiares(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    celular = models.CharField('Celular', max_length=50,unique=True)
    correo = models.EmailField('Email', max_length=50,unique=True)
    genero = models.CharField('Genero', max_length=50)
    parentesco = models.CharField('Parentesco', max_length=50)
    id_paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE)
    
    