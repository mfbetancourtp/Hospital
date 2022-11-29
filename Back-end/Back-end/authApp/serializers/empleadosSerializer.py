from authApp.models.empleados import Empleados
from rest_framework import serializers

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ['id_empleado', 'nombres', 'apellidos', 'cedula', 'correo', 'celular', 'direccion', 'cargo', 'contrasena']