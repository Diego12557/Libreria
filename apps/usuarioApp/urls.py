from django.urls import path
from .views import Login, RegistrarUsuario


urlpatterns = [
    path('login/', Login.as_view(), name = 'login'),
    path('', RegistrarUsuario.as_view(), name = 'registro')

]
