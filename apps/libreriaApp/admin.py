from django.contrib import admin
from .models import Autores,Categorias,Libros,PedidosCliente

admin.site.register(Autores)
admin.site.register(Categorias)
admin.site.register(Libros)
admin.site.register(PedidosCliente)

