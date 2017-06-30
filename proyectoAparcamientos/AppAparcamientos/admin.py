from django.contrib import admin

# Register your models here.
from AppAparcamientos.models import Aparcamiento
from AppAparcamientos.models import Comentario
#from AppAparcamientos.models import AparcamientoSeleccionado
from AppAparcamientos.models import Page_user

admin.site.register(Aparcamiento)
admin.site.register(Comentario)
#admin.site.register(AparcamientoSeleccionado)
admin.site.register(Page_user)
