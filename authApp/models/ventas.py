from django.db import models
from .user import User
from .productos import Productos

class Ventas (models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    fecha = models.DateTimeField()
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    productos = models.ForeignKey(Productos, related_name='productos', on_delete=models.CASCADE)
    


    