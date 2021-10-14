from django.db import models

class productos (models.Model):
    id_producto = models.IntegerField(primary_key=True)
    description = models.CharField('description', max_length = 256)
    price = models.IntegerField(default=0)

