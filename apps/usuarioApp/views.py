from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import FormLogin, FormUsuario

class Login(FormView):
    template_name = 'login.htm'
    form_class = FormLogin
    success_url =  reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("Usuario Ingresado")
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)




def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('accounts/login/')


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormUsuario
    template_name = 'registro.html'
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                identificacion = form.cleaned_data.get('identificacion'),
                nombre = form.cleaned_data.get('nombre'),
                apellido = form.cleaned_data.get('apellido'),
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                telefono = form.cleaned_data.get('telefono'),
                direccion = form.cleaned_data.get('direccion'),
                imagen = form.cleaned_data.get('imagen')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            
            if self.template_name == "registro.html":
                return render(request, 'registro_exitoso.html' )
            else:
                return redirect('usuario:listar_cliente')
        else:
            return render(request, self.template_name,{'form':form})