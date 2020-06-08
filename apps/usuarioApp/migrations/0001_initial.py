# Generated by Django 3.0.6 on 2020-06-08 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=150, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('email', models.CharField(max_length=50, verbose_name='Correo Electronico')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('imagen', models.ImageField(default='perfil/avatar.png', upload_to='perfil/', verbose_name='Imagen de Perfil')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
