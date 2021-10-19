from authApp.models.user                     import User
from authApp.models.ventas                   import Ventas
from rest_framework                          import serializers
from authApp.serializers.ventasSerializer    import VentasSerializer



class UserSerializer(serializers.ModelSerializer):
    ventas = VentasSerializer()


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'addres', 'email']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)



        return {
            "id": user.id,
            "username": user.username,
            "name": user.name,
            "addres": user.addres,
            "email": user.email,
          

             
        }