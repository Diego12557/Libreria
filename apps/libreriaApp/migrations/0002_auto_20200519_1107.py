# Generated by Django 3.0.6 on 2020-05-19 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreriaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autores',
            options={'managed': False, 'ordering': ['id_autor'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
    ]
