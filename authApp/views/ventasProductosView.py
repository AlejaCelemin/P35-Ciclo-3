from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated


from authApp.models.ventas import Ventas
from authApp.serializers.ventasSerializer import VentasSerializer

class VentasProductosView(generics.ListAPIView):
    serializer_class = VentasSerializer
   # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
 
        QuerySet = Ventas.objects.filter(productos_id=self.kwargs['productos'])        
        return QuerySet