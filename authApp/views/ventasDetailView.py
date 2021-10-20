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

class  VentasDetailView (generics.RetrieveAPIView):
    serializer_class =VentasSerializer
    queryset = Ventas.objects.all()

    def get(self, request, *args, **kwargs):



        return super().get(request, *args, **kwargs)