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

class ProductosDeleteView(generics.DestroyAPIView):
    serializer_class =ProductosSerializer
    queryset = Productos.objects.all()

    def delete(self, request, *args, **kwargs):
 

        return super().destroy(request, *args, **kwargs)