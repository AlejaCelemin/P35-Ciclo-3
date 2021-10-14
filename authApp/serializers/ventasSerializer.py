from django.db.models import fields
from authApp.models.ventas import ventas
from rest_framework          import serializers

class ventasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ventas
        fields = ['quantity', 'productos', 'facturas']