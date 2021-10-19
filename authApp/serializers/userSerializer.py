from authApp.models.user                     import User
from rest_framework                          import serializers




class UserSerializer(serializers.ModelSerializer):



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