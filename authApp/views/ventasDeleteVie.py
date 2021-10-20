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

class VentasDeleteView(generics.DestroyAPIView):
    serializer_class = VentasSerializer
    queryset = Ventas.objects.all()

    def deliete(self, request, *args, **kwargs):
        print ("Request:", request)
        print ("Args:", args)
        print("KWArgs:", kwargs)
       

        return super().destroy(request, *args, **kwargs)
