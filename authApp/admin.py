from django.contrib import admin

from .models.user import User
from .models.productos import Productos
from .models.ventas import Ventas

admin.site.register(User)
admin.site.register(Productos)
admin.site.register(Ventas)