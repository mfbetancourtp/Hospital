from rest_framework import serializers
from authApp.models.historiaclinica import Historia_Clinica


class HistoriaclinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia_Clinica
        fields = ['id_hc', 'fecha', 'code_patologia', 'tratamiento', 'cuidados', 'id_paciente', 'id_empleado',]