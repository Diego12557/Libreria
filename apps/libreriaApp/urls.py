from django.urls import path
from .views import (listar_autores, CrearAutor, EditarAutor, eliminarAutor, eliminar_categoria,
CrearCategorias,listar_categorias,EditarCategoria, listar_libro,CrearLibro, eliminar_libro,
EditarLibro,listar_pedido_cliente,CrearPedidoCliente,EditarPedidoCliente,EliminarPedidoCliente)

urlpatterns = [
   
   path('crear_autor/', CrearAutor.as_view(), name = 'crear_autor'),
   path('listar_autores/', listar_autores, name = 'listar_autores'),
   path('editar_autor/<int:pk>', EditarAutor.as_view(), name = 'editar_autor'),
   path('eliminar_autor/<int:id>', eliminarAutor, name = 'eliminar_autor'),
  
  
   path('crear_categorias/', CrearCategorias.as_view(), name = 'crear_categorias'),
   path('listar_categorias/', listar_categorias, name = 'listar_categorias'),
   path('editar_categorias/<int:pk>', EditarCategoria.as_view(), name = 'editar_categorias'),
   path('eliminar_categorias/<int:id_categoria>', eliminar_categoria, name = 'eliminar_categorias'),

  
   #path('crear_cliente/', CrearCliente.as_view(), name = 'crear_cliente'),
   #path('listar_cliente/', listar_cliente, name = 'listar_cliente'),
   #path('eliminar_cliente/<int:pk>', EliminarCliente.as_view(), name = 'eliminar_cliente'),
   #path('editar_cliente/<int:pk>', EditarCliente.as_view(), name = 'editar_cliente'),
   
   path('listar_libro/', listar_libro, name = 'listar_libro'),
   path('crear_libro/', CrearLibro.as_view(), name = 'crear_libro'),
   path('eliminar_libro/<int:isbn>', eliminar_libro, name = 'eliminar_libro'),
   path('editar_libro/<int:pk>', EditarLibro.as_view(), name = 'editar_libro'),


   path('listar_pedido_cliente/', listar_pedido_cliente, name = 'listar_pedido_cliente'),
   path('crear_pedido_cliente/', CrearPedidoCliente.as_view(), name = 'crear_pedido_cliente'),
   path('editar_pedido_cliente/<int:pk>', EditarPedidoCliente.as_view(), name = 'editar_pedido_cliente'),
   path('eliminar_pedido_cliente/<int:pk>', EliminarPedidoCliente.as_view(), name = 'eliminar_pedido_cliente'),

]