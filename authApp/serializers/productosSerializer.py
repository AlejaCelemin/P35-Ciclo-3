from django.db.models import fields
from authApp.models.productos import productos
from rest_framework          import serializers

class productosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = productos
        fields = ['description', 'price']