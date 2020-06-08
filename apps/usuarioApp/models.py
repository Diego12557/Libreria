from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombre, apellido, password = None):
        if not email:
            raise ValueError('El usuario debe tener un Correo')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nombre = nombre,
            apellido = apellido
        )
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, username, email, nombre, apellido, password):
        user = self.create_user(
            email,
            username = username,
            nombre = nombre,
            apellido = apellido,
            password = password
        )

        user.usuario_administrador = True
        user.save()

        return user

class Usuario(AbstractBaseUser):
    nombre = models.CharField('nombre', max_length=150)
    apellido = models.CharField('apellido', max_length=50)
    email = models.CharField('Correo Electronico', max_length=50)
    username = models.CharField( max_length=50, unique = True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=100, blank = False, null = False, default ='perfil/avatar.png')
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'email']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    def has_perm(self, perm, obj = None):
        return True



    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador