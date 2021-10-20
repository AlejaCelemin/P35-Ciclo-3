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

class VentasUpdateView (generics.UpdateAPIView):
    serializer_class = VentasSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Ventas.objects.all()

    def update (self, request, *args, **kwargs):


        
        return super().update(request, *args, **kwargs)








