from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import AutorForm,CategoriaForm,ClienteForm,LibroForm,PedidoClienteForm
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Autores,Categorias,Cliente,Libros,PedidosCliente
from django.contrib.auth.mixins import LoginRequiredMixin





def Home(request):
    return render(request, 'index.htm') 



class CrearAutor(CreateView):
    model = Autores
    form_class = AutorForm
    template_name = 'libreriaApp/autores/crear_autor.htm'
    success_url = reverse_lazy('libreriaApp:listar_autores')


def editarAutor(request, id):
    pass



def eliminarAutor(request, id):
    autor = Autores.objects.get(id_autor = id)
    autor.delete()
    return redirect('libreriaApp:listar_autores') 

def listar_autores(request):
    autores = Autores.objects.all()
    return render(request, 'libreriaApp/autores/listar_autor.htm',{'autores':autores})



class CrearCategorias(CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'libreriaApp/categorias/crear_categorias.htm'
    success_url = reverse_lazy('libreriaApp:listar_categorias')


def listar_categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'libreriaApp/categorias/listar_categorias.htm',{'categorias':categorias})


class EditarCategoria(UpdateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'libreriaApp/categorias/editar_categorias.htm'
    success_url = reverse_lazy('libreriaApp:listar_categorias')


class EliminarCategoria(DeleteView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'libreriaApp/categorias/eliminar_categoria.htm'
    success_url = reverse_lazy('libreriaApp:listar_categorias')



class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'libreriaApp/clientes/crear_cliente.htm'
    success_url = reverse_lazy('libreriaApp:listar_cliente')


def listar_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'libreriaApp/clientes/listar_cliente.htm',{'cliente':cliente})


class EliminarCliente(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'libreriaApp/clientes/eliminar_cliente.htm'
    success_url = reverse_lazy('libreriaApp:listar_cliente')


class EditarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'libreriaApp/clientes/editar_cliente.htm'
    success_url = reverse_lazy('libreriaApp:listar_cliente')




def listar_libro(request):
    libro = Libros.objects.all()
    return render(request, 'libreriaApp/libro/listar_libro.htm',{'libro':libro})


class CrearLibro(CreateView):
    model = Libros
    form_class = LibroForm
    template_name = 'libreriaApp/libro/crear_libro.htm'
    success_url = reverse_lazy('libreriaApp:listar_libro')


class EliminarLibro(DeleteView):
    model = Libros
    form_class = LibroForm
    template_name = 'libreriaApp/libro/eliminar_libro.htm'
    success_url = reverse_lazy('libreriaApp:listar_libro')


class EditarLibro(UpdateView):
    model = Libros
    form_class = LibroForm
    template_name = 'libreriaApp/libro/editar_libro.htm'
    success_url = reverse_lazy('libreriaApp:listar_libro')




def listar_pedido_cliente(request):
    pedido_cliente = PedidosCliente.objects.all()
    return render(request, 'libreriaApp/pedido_cliente/listar_pedido_cliente.htm',{'pedido_cliente':pedido_cliente})


class CrearPedidoCliente(CreateView):
    model = PedidosCliente
    form_class = PedidoClienteForm
    template_name = 'libreriaApp/pedido_cliente/crear_pedido_cliente.htm'
    success_url = reverse_lazy('libreriaApp:listar_pedido_cliente')


class EditarPedidoCliente(UpdateView):
    model = PedidosCliente
    form_class = PedidoClienteForm
    template_name = 'libreriaApp/pedido_cliente/editar_pedido_cliente.htm'
    success_url = reverse_lazy('libreriaApp:listar_pedido_cliente')


class EliminarPedidoCliente(DeleteView):
    model = PedidosCliente
    form_class = PedidoClienteForm
    template_name = 'libreriaApp/pedido_cliente/eliminar_pedido_cliente.htm'
    success_url = reverse_lazy('libreriaApp:listar_pedido_cliente')

    











