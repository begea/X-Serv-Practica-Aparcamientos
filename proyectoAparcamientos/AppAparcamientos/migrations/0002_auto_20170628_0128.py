# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-28 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAparcamientos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aparcamientoseleccionado',
            name='Aparcamiento',
        ),
        migrations.RemoveField(
            model_name='imagen',
            name='image',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='comment',
            new_name='aparcamiento_comentado',
        ),
        migrations.RenameField(
            model_name='page_user',
            old_name='background',
            new_name='color_page',
        ),
        migrations.RenameField(
            model_name='page_user',
            old_name='size',
            new_name='tamano_letra',
        ),
        migrations.RenameField(
            model_name='page_user',
            old_name='title_page',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='page_user',
            old_name='username',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='accessibility',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='contact_info',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='description',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='district',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='name',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='h_id',
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='accessibilidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='barrio',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='clasevial',
            field=models.CharField(default='Null', max_length=20),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='codpostal',
            field=models.CharField(default='Null', max_length=10),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='coordenadax',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='coordenaday',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='descripcion',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='direccion',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='distrito',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='email',
            field=models.CharField(default='Null', max_length=75),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='entidad',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='latitud',
            field=models.CharField(default='Null', max_length=25),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='localidad',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='longitud',
            field=models.CharField(default='Null', max_length=25),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='nombre',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='nombrevia',
            field=models.CharField(default='Null', max_length=20),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='numcomentarios',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='numvia',
            field=models.CharField(default='Null', max_length=10),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='provincia',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='telefono',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='page_user',
            name='Aparc_Selec',
            field=models.ManyToManyField(to='AppAparcamientos.Aparcamiento'),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='url',
            field=models.URLField(default='Null'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(default='Null'),
        ),
        migrations.DeleteModel(
            name='AparcamientoSeleccionado',
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]