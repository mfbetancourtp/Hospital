from rest_framework import serializers
from authApp.models.pacientes import Pacientes


class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = ['id_paciente', 'nombres', 'apellidos', 'tipo_de_identificacion', 'nro_identificacion', 'email', 'celular', 'id_usuario', 'id_empleado']