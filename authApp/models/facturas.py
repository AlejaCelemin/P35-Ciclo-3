from django.db import models
from .user import User


class facturas (models.Model):
    id_bill = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    user = models.ForeignKey(User, related_name='facturas', on_delete=models.CASCADE)
  
    