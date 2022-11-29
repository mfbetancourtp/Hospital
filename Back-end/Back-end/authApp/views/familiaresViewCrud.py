from rest_framework.response import Response
from rest_framework.decorators import api_view
from authApp.models import Familiares
from authApp.serializers import FamiliaresSerializer

@api_view(['GET','POST'])
def Familiares_api_view(request):
    if request.method == 'GET':
        familiar = Familiares.objects.all()
        Familiares_serializer = FamiliaresSerializer(familiar,many=True)
        return Response(Familiares_serializer.data)

    elif request.method == 'POST':
        Familiares_serializer = FamiliaresSerializer(data = request.data)
        if Familiares_serializer.is_valid():
            Familiares_serializer.save()
            return Response(Familiares_serializer.data)
        return Response(Familiares_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Familiares_detail_view(request,pk=None):
    
    if request.method == 'GET':
        familiar = Familiares.objects.filter(id = pk).first()
        Familiares_serializer = FamiliaresSerializer(familiar)
        return Response(Familiares_serializer.data)

    elif request.method == 'PUT':
       familiar = Familiares.objects.filter(id = pk).first() 
       Familiares_serializer = FamiliaresSerializer(instance=familiar, data = request.data)
       if Familiares_serializer.is_valid():
            Familiares_serializer.save()
            return Response(Familiares_serializer.data)

