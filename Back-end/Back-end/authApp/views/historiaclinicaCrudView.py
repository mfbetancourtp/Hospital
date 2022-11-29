from rest_framework.response import Response
from rest_framework.decorators import api_view
from authApp.models import Historia_Clinica
from authApp.serializers import HistoriaclinicaSerializer


@api_view(['GET','POST'])
def Historia_Clinica_api_view(request):
    if request.method == 'GET':
        historiaClinica = Historia_Clinica.objects.all()
        Historia_Clinica_Serializer = HistoriaclinicaSerializer(historiaClinica,many=True)
        return Response(Historia_Clinica_Serializer.data)

    elif request.method == 'POST':
        Historia_Clinica_Serializer = HistoriaclinicaSerializer(data = request.data)
        if Historia_Clinica_Serializer.is_valid():
            Historia_Clinica_Serializer.save()
            return Response(Historia_Clinica_Serializer.data)
        return Response(Historia_Clinica_Serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Historia_Clinica_detail_view(request,pk=None):
    
    if request.method == 'GET':
        historiaClinica = Historia_Clinica.objects.filter(id = pk).first()
        Historia_Clinica_Serializer = HistoriaclinicaSerializer(historiaClinica)
        return Response(Historia_Clinica_Serializer.data)

    elif request.method == 'PUT':
       historiaClinica = Historia_Clinica.objects.filter(id = pk).first() 
       Historia_Clinica_Serializer = HistoriaclinicaSerializer(instance=historiaClinica, data = request.data)
       if Historia_Clinica_Serializer.is_valid():
            Historia_Clinica_Serializer.save()
            return Response(Historia_Clinica_Serializer.data)

    elif request.method == 'DELETE':
        historiaClinica = Historia_Clinica.objects.filter(id = pk).first()
        historiaClinica.delete()
        return Response("Eliminado...")