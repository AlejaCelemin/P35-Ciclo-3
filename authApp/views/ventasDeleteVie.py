from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated


from authApp.models.ventas import Ventas
from authApp.serializers.ventasSerializer import VentasSerializer



class  VentasDetailView (generics.RetrieveAPIView):
    serializer_class =VentasSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Ventas.objects.all()

    def get(self, request, *args, **kwargs):
        print("Request:",request)
        print("Args",args)
        print("KWArgs:",kwargs)
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

    


class VentasUpdateView (generics.UpdateAPIView):
    serializer_class = VentasSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Ventas.objects.all()

    def update (self, request, *args, **kwargs):
        print("Request:",request)
        print("Args:", args)
        print("KWArgs:", kwargs)
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().update(request, *args, **kwargs)

class VentasDeleteView(generics.DestroyAPIView):
    serializer_class = VentasSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Ventas.objects.all()

    def deliete(self, request, *args, **kwargs):
        print ("Request:", request)
        print ("Args:", args)
        print("KWArgs:", kwargs)
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)