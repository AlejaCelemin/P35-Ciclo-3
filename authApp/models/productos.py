from django.db import models

class Productos (models.Model):
    id_producto = models.CharField('id_producto', max_length = 30, unique=True ,primary_key=True)
    description = models.CharField('description', max_length = 256)
    price = models.IntegerField(default=0)

