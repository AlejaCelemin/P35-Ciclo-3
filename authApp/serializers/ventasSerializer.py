from django.db.models import fields
from authApp.models.ventas import Ventas
from rest_framework          import serializers

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Ventas
        fields = ['quantity', 'fecha']