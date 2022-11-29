from rest_framework.response import Response
from rest_framework.decorators import api_view
from authApp.models import Pacientes
from authApp.serializers import PacientesSerializer

@api_view(['GET','POST'])
def Pacientes_api_view(request):
    if request.method == 'GET':
        paciente = Pacientes.objects.all()
        Pacientes_serializer = PacientesSerializer(paciente,many=True)
        return Response(Pacientes_serializer.data)

    elif request.method == 'POST':
        Pacientes_serializer = PacientesSerializer(data = request.data)
        if Pacientes_serializer.is_valid():
            Pacientes_serializer.save()
            return Response(Pacientes_serializer.data)
        return Response(Pacientes_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Pacientes_detail_view(request,pk=None):
    
    if request.method == 'GET':
        paciente = Pacientes.objects.filter(id = pk).first()
        Pacientes_serializer = PacientesSerializer(paciente)
        return Response(Pacientes_serializer.data)

    elif request.method == 'PUT':
       paciente = Pacientes.objects.filter(id = pk).first() 
       Pacientes_serializer = PacientesSerializer(instance=paciente, data = request.data)
       if Pacientes_serializer.is_valid():
            Pacientes_serializer.save()
            return Response(Pacientes_serializer.data)

   