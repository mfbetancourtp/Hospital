from django.db import models
from .pacientes import Pacientes
from .empleados import Empleados

class Historia_Clinica(models.Model):
    id_hc=models.AutoField(primary_key=True)
    fecha=models.CharField(max_length=100)
    code_patologia=models.CharField(max_length=15)
    tratamiento=models.CharField(max_length=50)
    cuidados=models.CharField(max_length=50)
    id_paciente=models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    id_empleado=models.ForeignKey(Empleados, on_delete=models.CASCADE)