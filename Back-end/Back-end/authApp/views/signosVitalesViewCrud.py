from rest_framework.response import Response
from rest_framework.decorators import api_view
from authApp.models import SignosVitales
from authApp.serializers import SignosVitalesSerializer

@api_view(['GET','POST'])
def SignosVitales_api_view(request):
    if request.method == 'GET':
        signoVital = SignosVitales.objects.all()
        SignosVitales_serializer = SignosVitalesSerializer(signoVital,many=True)
        return Response(SignosVitales_serializer.data)

    elif request.method == 'POST':
        SignosVitales_serializer = SignosVitalesSerializer(data = request.data)
        if SignosVitales_serializer.is_valid():
            SignosVitales_serializer.save()
            return Response(SignosVitales_serializer.data)
        return Response(SignosVitales_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def SignosVitales_detail_view(request,pk=None):
    
    if request.method == 'GET':
        signoVital = SignosVitales.objects.filter(id = pk).first()
        SignosVitales_serializer = SignosVitalesSerializer(signoVital)
        return Response(SignosVitales_serializer.data)

    elif request.method == 'PUT':
       signoVital = SignosVitales.objects.filter(id = pk).first() 
       SignosVitales_serializer = SignosVitalesSerializer(instance=signoVital, data = request.data)
       if SignosVitales_serializer.is_valid():
            SignosVitales_serializer.save()
            return Response(SignosVitales_serializer.data)
