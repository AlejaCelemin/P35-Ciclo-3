from authApp.models.user                     import User
from authApp.models.ventas                   import Ventas
from rest_framework                          import serializers
from authApp.serializers.ventasSerializer    import VentasSerializer



class UserSerializer(serializers.ModelSerializer):
    ventas = VentasSerializer()


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'addres', 'email','ventas']

    def create(self, validated_data):
        ventasData = validated_data.pop('ventas')
        userInstance = User.objects.create(**validated_data)
        Ventas.objects.create(user=userInstance, **ventasData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        ventas = Ventas.objects.get(user=obj.id)


        return {
            "id": user.id,
            "username": user.username,
            "name": user.name,
            "addres": user.addres,
            "email": user.email,
            'ventas': {
                 "id": ventas.id,
                 "quantity":ventas.quantity,
                 "fecha":ventas.fecha            

             }
        }