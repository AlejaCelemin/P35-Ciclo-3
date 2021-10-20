from django.db.models import fields
from authApp.models.productos import Productos
from rest_framework          import serializers

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Productos
        fields = ['id_producto', 'description','price']



