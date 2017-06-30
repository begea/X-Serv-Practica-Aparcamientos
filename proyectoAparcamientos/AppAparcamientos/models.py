from django.db import models
# Create your models here.

class Aparcamiento (models.Model):
    nombre = models.CharField(max_length=100, default="Null")
    url = models.URLField(default="Null")
    descripcion = models.TextField(default="Null")
    accesibilidad = models.IntegerField(default=0)
    distrito = models.CharField(max_length=50, default="Null")
    latitud = models.CharField(max_length=25, default="Null")
    longitud = models.CharField(max_length=25, default="Null")
    barrio = models.CharField(max_length=50, default="Null")
    codpostal = models.CharField(max_length=10, default="Null")
    entidad = models.CharField(max_length=200, default="Null")
    clasevial = models.CharField(max_length=20, default="Null")
    nombrevia = models.CharField(max_length=20, default="Null")
    numvia = models.CharField(max_length=10, default="Null")
    telefono = models.CharField(max_length=50, default="Null")
    email = models.CharField(max_length=75, default="Null")
    numcomentarios = models.IntegerField(default=0)

class Comentario (models.Model):
    aparcamiento_comentado = models.CharField(max_length=10, default="Null")
    text = models.TextField(default="Null")
    date = models.DateTimeField(auto_now_add=True)

#class AparcamientoSeleccionado (models.Model):
#    username = models.CharField(max_length=300,default="")
#    Aparcamiento = models.ForeignKey(Aparcamiento)
#    date = models.DateField(auto_now=True)

class Page_user (models.Model):
    usuario = models.CharField(max_length=300,default="")
    titulo = models.CharField(max_length=300,default="")
    background = models.CharField(max_length=300,default="")
    size = models.CharField(max_length=200,default="")
    Aparc_Selec = models.ManyToManyField(Aparcamiento)
