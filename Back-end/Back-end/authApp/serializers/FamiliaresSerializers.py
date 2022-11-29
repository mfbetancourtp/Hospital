from rest_framework import serializers
from authApp.models.familiar import Familiares


class FamiliaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiares
        fields = ['id_familiar', 'nombres', 'apellidos', 'celular', 'correo', 'genero','celular', 'parentesco', 'id_paciente']
