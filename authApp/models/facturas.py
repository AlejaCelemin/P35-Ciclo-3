from django.db import models
from .clientes import User


class facturas (models.Model):
    id_bill = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    clientes = models.ForeignKey(User, related_name='facturas', on_delete=models.CASCADE)
  
    