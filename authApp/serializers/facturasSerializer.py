from django.db.models import fields
from authApp.models.facturas import facturas
from rest_framework          import serializers

class facturasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = facturas
        fields = ['fecha']