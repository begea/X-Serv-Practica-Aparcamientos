
from django.conf.urls import include, url
from django.views.static import serve
from django.contrib import admin
from AppAparcamientos import views
from django.contrib.auth.views import login, logout
from proyectoAparcamientos import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'static/(?P<path>.*)$', serve, {'document_root': settings.URL_INICIAL}),
    url(r'css/(.+)$', views.css, name="Cargar el documento CSS"),
    url(r'^$',views.inicio, name = "Página principal del sitio"),
    url(r'^about/$',views.about, name = "Página de información"),
    url(r'^(.*)/xml$', views.xml_inicio, name = "XML de la página principal del sitio"),
    url(r'^aparcamientos/$', views.pagina_aparcamientos, name = "Página sobre todos los aparcamientos"),
    url(r'^aparcamientos/(\d+)$',views.pagina_aparcamiento, name = "Página de un aparcamiento"),
    url(r'^login', views.milogin),
    url(r'^logout', logout, {'next_page': '/'}),
    url(r'^register/$', views.register, name = "Crear un usuario"),
    url(r'^(.+)$', views.page_usu, name = "Pagina personal del usuario"),
]
