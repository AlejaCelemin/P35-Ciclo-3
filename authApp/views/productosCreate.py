from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.productos import Productos
from authApp.serializers.productosSerializer import ProductosSerializer

class ProductosCreateView(generics.CreateAPIView):
    serializer_class =ProductosSerializer


    def post(self, request, *args, **kwargs):
        print("Request",request)
        print("Args", args)
        print("KWArgs", kwargs)
  
            
        serializer = ProductosSerializer(data = request.data['productos_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Producto creado", status=status.HTTP_201_CREATED)



    