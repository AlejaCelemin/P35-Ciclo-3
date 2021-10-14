from django.db import models
from .clientes import User

class facturas (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    fecha = models.DateTimeField()
    isActive = models.BooleanField(default=True)