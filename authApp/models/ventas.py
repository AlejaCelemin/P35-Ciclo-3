from django.db import models
from .user import User
from .facturas import facturas
from .productos import productos

class ventas (models.Model):
    id_venta = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='ventas', on_delete=models.CASCADE)
    productos = models.ForeignKey(productos, related_name='ventas', on_delete=models.CASCADE)
    facturas = models.ForeignKey(facturas, related_name='ventas', on_delete=models.CASCADE)


    