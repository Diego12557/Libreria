from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import AutorForm,CategoriaForm,LibroForm,PedidoClienteForm
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Autores,Categorias, Libros,PedidosCliente
from django.contrib.auth.mixins import LoginRequiredMixin





def Home(request):
    pedidos = PedidosCliente.objects.filter(id_cliente = request.user.id)
    return render(request, 'index.htm', {'pedidos':pedidos}) 



class CrearAutor(CreateView):
    model = Autores
    form_class = AutorForm
    template_name = 'libreriaApp/autores/crear_autor.htm'
    success_url = reverse_lazy('libreriaApp:listar_autores')

    def get(self, request, *args, **kwars):
        pedidos = PedidosCliente.objects.filter(id_cliente = request.user.id)
        return render(request, self.template_name, {'pedidos':pedidos})


class EditarAutor(UpdateView):
    model = Autores
    form_class = AutorForm
    template_name = 'libreriaApp/autores/crear_autor.htm'
    success_url = reverse_lazy('libreriaApp:listar_autores')


def eliminarAutor(request, id):
    autor = Autores.objects.get(id_autor = id)
    autor.delete()
    return redirect('libreriaApp:listar_autores') 

def listar_autores(request):
    autores = Autores.objects.all()
    pedidos = PedidosCliente.objects.filter(id_cliente = request.user.id)

    context = {
        'autores': autores,
        'pedidos': pedidos
    }
    return render(request, 'libreriaApp/autores/listar_autor.htm', context)



class CrearCategorias(CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'libreriaApp/categorias/crear_categorias.htm'
    success_url = reverse_lazy('libreriaApp:listar_categorias')

    def get(self, request, *args, **kwars):
        pedidos = PedidosCliente.objects.filter(id_cliente = request.user.id)
        return render(request, self.template_name, {'pedidos':pedidos})


class EditarCategoria(UpdateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'libreriaApp/categorias/crear_categorias.htm'
    success_url = reverse_lazy('libreriaApp:listar_categorias')


def eliminar_categoria(request, id_categoria):
    autor = Categorias.objects.get(id_categoria = id_categoria)
    autor.delete()
    return redirect('libreriaApp:listar_categorias') 

def listar_categorias(request):
    categorias = Categorias.objects.all()
    pedidos = PedidosCliente.objects.filter(id_cliente = request.user.id)

    context = {
        'categorias':categorias,
        'pedidos': pedidos
    }
    return render(request, 'libreriaApp/categorias/listar_categorias.htm',context)



""" 

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


 """

def listar_libro(request):
    libro = Libros.objects.all()
    pedidos = PedidosCliente.objects.filter(id_cliente = request.user.id)

    context = {
        'libro': libro,
        'pedidos': pedidos
    }
    return render(request, 'libreriaApp/libro/listar_libro.htm', context)


class CrearLibro(CreateView):
    model = Libros
    form_class = LibroForm
    template_name = 'libreriaApp/libro/crear_libro.htm'
    success_url = reverse_lazy('libreriaApp:listar_libro')

def eliminar_libro(request, isbn):
    libro = Libros.objects.get(isbn = isbn)
    libro.delete()

    return redirect('libreriaApp:listar_libro')


class EditarLibro(UpdateView):
    model = Libros
    form_class = LibroForm
    template_name = 'libreriaApp/libro/crear_libro.htm'
    success_url = reverse_lazy('libreriaApp:listar_libro')




def listar_pedido_cliente(request):
    pedido_cliente = PedidosCliente.objects.all()
    pedidos = PedidosCliente.objects.filter(id_cliente = request.user.id)

    context = {
        'pedido_cliente':pedido_cliente,
        'pedidos': pedidos
    }
    return render(request, 'libreriaApp/pedido_cliente/listar_pedido_cliente.htm',context)


class CrearPedidoCliente(CreateView):
    model = PedidosCliente
    form_class = PedidoClienteForm
    template_name = 'libreriaApp/pedido_cliente/listar_pedido_cliente.htm'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            isbn_libro = form.cleaned_data.get('isbn').isbn
            cantidad = int(form.cleaned_data.get('cantidad'))
            precio_libro = int(Libros.objects.get(isbn = isbn_libro).precio)
            valor_pedido = cantidad*precio_libro

            nuevo_pedido = PedidosCliente(
                id_cliente = form.cleaned_data.get('id_cliente'),
                isbn = form.cleaned_data.get('isbn'),
                cantidad = form.cleaned_data.get('cantidad'),
                valor = valor_pedido
            )

            nuevo_pedido.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, 'libreriaApp/libro/listar_libro.htm', {'form':form})


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

    











