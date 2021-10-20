from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authApp.models.productos import Productos


from authApp.models.ventas import Ventas
from authApp.serializers.ventasSerializer import VentasSerializer

class VentasCreateView(generics.CreateAPIView):
    serializer_class = VentasSerializer
   # permission_classes =(IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        """token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
"""
        productos = Productos.objects.get(id=request.data['ventas_data']['productos'])
        productos.save() 



        serializer = VentasSerializer(data=request.data['ventas_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Venta exitosa", status=status.HTTP_201_CREATED)