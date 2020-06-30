from django.db import models
from apps.usuarioApp.models import Usuario

class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=25, blank = False, null = False)
    nombres = models.CharField(max_length=25, blank = False, null = False)

    class Meta:
        ordering = ['id_autor']

    def __str__(self):
        return self.nombres +" "+ self.apellidos



class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=40, blank = False, null = False)

    class Meta:
        ordering = ['id_categoria']

    def __str__(self):
      return '{} - {}'.format(
            self.id_categoria,
            self.categoria
        )



class Libros(models.Model):
    isbn = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=128, blank = False, null = False)
    fecha_pub = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
    precio = models.IntegerField()
    portada = models.ImageField('Imagen de Portada', upload_to='portada/', max_length=200, blank = True,null = True, default='')
    id_autor = models.ManyToManyField(Autores)
    
    class Meta:
        ordering = ['isbn']

    def __str__(self):
        return '{} - {} - {}'.format(
            self.isbn,
            self.titulo,
            "$"+str(self.precio)
        )


class PedidosCliente(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    isbn = models.ForeignKey(Libros, on_delete = models.CASCADE)
    fecha_pedido = models.DateField(auto_now = True, auto_now_add = False)
    cantidad = models.IntegerField()
    valor = models.IntegerField(blank = True, null = True)

    class Meta:
        ordering = ['id_pedido']

    def __str__(self):
        return '{} - {} - {} - {} '.format(
            self.id_cliente,
            self.isbn,
            self.cantidad,
            self.valor
        )