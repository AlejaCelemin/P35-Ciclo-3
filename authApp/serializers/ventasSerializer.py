from django.db.models import fields
from authApp.models import productos
from authApp.models import user
from authApp.models.productos import Productos
from authApp.models.ventas import Ventas
from rest_framework          import serializers
from authApp.models.user import User

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Ventas
        fields = ['id','quantity', 'fecha','user','productos']

    def create(self, validated_data):
        productos_data = validated_data.pop('productos')
        user_data = validated_data.pop('user')
        ventainstancia = Ventas.objects.create(**validated_data)
        Productos.objects.create(ventas = ventainstancia,**productos_data)
        User.objects.create(ventas = ventainstancia, **user_data)

        return ventainstancia

    def to_representation(self, obj):
        productos = Productos.objects.get(id=obj.productos)
        ventas    = Ventas.objects.get(id=obj.id)
        user      = User.objects.get(id=obj.id)

        return {

            
            "id": ventas.id,
            "quantity": ventas.quantity,
            "fecha": ventas.fecha,
            "user": user.id,
            "producto": productos.id_producto
                 

            
        }
