from django.contrib import admin

from .models.user import User
from .models.facturas import facturas
from .models.productos import productos
from .models.ventas import ventas

admin.site.register(User)
admin.site.register(facturas)
admin.site.register(productos)
admin.site.register(ventas)