from django.contrib import admin
from .models import Autores,Categorias,Cliente,Libros,PedidosCliente

admin.site.register(Autores)
admin.site.register(Categorias)
admin.site.register(Cliente)
admin.site.register(Libros)
admin.site.register(PedidosCliente)

