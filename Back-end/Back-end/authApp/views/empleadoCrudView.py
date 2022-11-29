from rest_framework.response import Response
from rest_framework.decorators import api_view
from authApp.models import Empleados
from authApp.serializers import EmpleadosSerializer
from urllib import request


@api_view(['GET','POST'])
def empleado_api_view(request):
    if request.method == 'GET':
        empleado = Empleados.objects.all()
        empleados_serializer = EmpleadosSerializer(empleado,many=True)
        return Response(empleados_serializer.data)

    elif request.method == 'POST':
        empleados_serializer = EmpleadosSerializer(data = request.data)
        if empleados_serializer.is_valid():
            empleados_serializer.save()
            return Response(empleados_serializer.data)
        return Response(empleados_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def empleado_detail_view(request,pk=None):
    
    if request.method == 'GET':
        empleado = Empleados.objects.filter(id = pk).first()
        empleados_serializer = EmpleadosSerializer(empleado)
        return Response(empleados_serializer.data)

    elif request.method == 'PUT':
       empleado = Empleados.objects.filter(id = pk).first() 
       empleados_serializer = EmpleadosSerializer(instance=empleado, data = request.data)
       if empleados_serializer.is_valid():
            empleados_serializer.save()
            return Response(empleados_serializer.data)

    elif request.method == 'DELETE':
        empleado = Empleados.objects.filter(id = pk).first()
        empleado.delete()
        return Response("Eliminado...")