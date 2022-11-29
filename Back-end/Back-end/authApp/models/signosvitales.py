from django.db import models
from .pacientes import Pacientes

class SignosVitales(models.Model):
    id_sgnvital = models.AutoField(primary_key=True)
    fecha = models.CharField('Fecha', max_length = 20)
    oximetria = models.CharField('Oximetría', max_length = 10)
    frecuencia_respiratoria = models.CharField('Frecuencia respiratoria', max_length = 10)
    frecuencia_cardiaca  = models.CharField('Frecuencia cardiaca', max_length = 10)
    temperatura = models.CharField('Temperatura', max_length = 10)
    presion_arterial  = models.CharField('Presion Arterial', max_length = 10)
    glicemia  = models.CharField('contrasena', max_length = 10)
    id_paciente  = models.ForeignKey(Pacientes, on_delete=models.CASCADE)