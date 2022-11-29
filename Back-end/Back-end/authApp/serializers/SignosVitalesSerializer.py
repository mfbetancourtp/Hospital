from rest_framework import serializers
from authApp.models.signosvitales import SignosVitales


class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ['id_sgnvital', 'fecha', 'oximetria', 'frecuencia_respiratoria', 'frecuencia_cardiaca', 'temperatura', 'presion_arterial', 'glicemia', 'id_paciente']