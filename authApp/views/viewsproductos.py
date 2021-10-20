from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.productos import Productos
from authApp.serializers.productosSerializer import ProductosSerializer

class ProductosCreateView(generics.CreateAPIView):
    serializer_class =ProductosSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print("Request",request)
        print("Args", args)
        print("KWArgs", kwargs)
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 

        serializer = ProductosSerializer(data = request.data['productos_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Producto creado", status=status.HTTP_201_CREATED)


class ProductosDeleteView(generics.DestroyAPIView):
    serializer_class =ProductosSerializer
    permission_classes =(IsAuthenticated,)
    queryset = Productos.objects.all()

    def get(self, request, *args, **kwargs):
        print("Request",request)
        print("Args", args)
        print("KWArgs", kwargs)
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 

        return super().destroy(request, *args, **kwargs)
    