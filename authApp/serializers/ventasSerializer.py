from django.db.models import fields
from authApp.models import productos
from authApp.models.productos import Productos
from authApp.models.ventas import Ventas
from rest_framework          import serializers

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Ventas
        fields = ['quantity', 'fecha','productos']

    def to_representation(self, obj):
        productos = Productos.objects.get(id=obj.productos)
        ventas    = Ventas.objects.get(id=obj.id)

        return {

            "id": ventas.id,
            "quantity": ventas.quantity,
            "fecha": ventas.fecha,

            "productos": {
                 "id_producto": productos.id_producto,
                 "description":productos.description,
                 "price":productos.price
            }
        }
