from django.shortcuts import render
import math
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
import urllib.request
from AppAparcamientos.models import Aparcamiento
from AppAparcamientos.models import Page_user
#from AppAparcamientos.models import AparcamientoSeleccionado
from AppAparcamientos.models import Comentario
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render_to_response

<<<<<<< HEAD
def formulario_logear(request):
    if request.user.is_authenticated():
        response = "<p>Logeado como " + request.user.username
        response += "<a href='/logout'> Logout </a></p>"
    else:
        response = "<form action='/login' method='post'>"
        response += "user: <input type= 'text' name='user'>"
        response += "password: <input type= 'password' name='password'>"
        response += "<input type= 'submit' value='enviar'>"
        response += "</form>"
        response += "<a href='/register/'>Registrar</a>"
    return response

@csrf_exempt
def milogin(request):
    user = request.POST['user']
    password = request.POST['password']
    user = authenticate(username=user, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/')

#@csrf_exempt
#def milogout(request):
#    if request.method == 'POST':
#        logout(request)
#    return redirect('/')

def lista_users(request):
    # Esto es para ver la nombre de lso usuarios guardados
    list_usu = ""
    lista_pag = Page_user.objects.all()
    for i in lista_pag:
        list_usu += "<br><a href=" + i.usuario + ">" + i.titulo
        list_usu += "</a> " + i.usuario

    return list_usu

@csrf_exempt
def register(request):
    if request.method == "GET":
        formulario = "Registra otro usuario: "
        formulario += "<form action='/register/' method='post'>"
        formulario += "Name: <input type= 'text' name='user'>"
        formulario += "Correo: <input type= 'text' name='email'>"
        formulario += "Password: <input type= 'password' name='password'>"
        formulario += "<input type= 'submit' value='Registrar'>"
        formulario += "</form>"
    elif request.method == "POST":
        user = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(user, email, password)
        user.save()
        URL = "http://localhost:1234/"
        return redirect(URL)
    else:
        formulario = "No estas registrandote como debes."

    template = get_template("carpeta_plantillas/register.html")
    cont = Context({'content': formulario})
    response = template.render(cont)
    return HttpResponse(response, content_type="text/html")

def refresh_users(request):
    lista_users = User.objects.all()
    lista_pag = Page_user.objects.all()
    for usuario in lista_users:
        if len(lista_pag) == 0:
            usua = usuario.get_username()
            title = "Pagina de " + usuario.get_username()
            Pag_usu = Page_user(usuario=usua, titulo=title)
            Pag_usu.save()
        else:
            contador = 0
            for pag in lista_pag:
                if pag.usuario == usuario.get_username():
                    break
                elif pag.usuario != usuario.get_username() and contador == len(lista_pag)-1:
                    usua = usuario.get_username()
                    title = "Pagina de " + usuario.get_username()
                    Pag_usu = Page_user(usuario=usua, titulo=title)
                    Pag_usu.save()
                    break
                else:
                    contador = contador + 1

def parser(request):
    pagina = 'http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c'
    pagina += '31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a'
    pagina += '0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-resident'
    pagina += 'es&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full'
    archivo = urllib.request.urlopen(pagina).read()
    soup = BeautifulSoup(archivo, 'html.parser')

    for i in soup.findAll('contenido'):
        name = i.find(nombre='NOMBRE').next_element
        entity = i.find(nombre='ID-ENTIDAD').next_element
        if i.find(nombre='DESCRIPCION') is None:
            description = "Null"
        else:
            description = i.find(nombre='DESCRIPCION').next_element

        accesibility = i.find(nombre='ACCESIBILIDAD').next_element
        enlace = i.find(nombre='CONTENT-URL').next_element
        classvial = i.find(nombre='CLASE-VIAL').next_element
        namevia = i.find(nombre='NOMBRE-VIA').next_element

        if i.find(nombre='CODIGO-POSTAL') is None:
            cod_postal = "Null"
        else:
            cod_postal = i.find(nombre='CODIGO-POSTAL').next_element
        if i.find(nombre='NUM') is None:
            num_via = 0
        else:
            num_via = i.find(nombre='NUM').next_element
        if i.find(nombre='BARRIO') is None:
            neighborhood = "Null"
        else:
            neighborhood = i.find(nombre='BARRIO').next_element
        if i.find(nombre='DISTRITO') is None:
            district = "Null"
        else:
            district = i.find(nombre='DISTRITO').next_element
        if i.find(nombre='LATITUD') is None:
            latitude = "Null"
        else:
            latitude = i.find(nombre='LATITUD').next_element
        if i.find(nombre='LONGITUD') is None:
            longitude = "Null"
        else:
            longitude = i.find(nombre='LONGITUD').next_element
        if i.find(nombre='TELEFONO') is None:
            phone = "Null"
        else:
            phone = i.find(nombre='TELEFONO').next_element
        if i.find(nombre='EMAIL') is None:
            correo = "Null"
        else:
            correo = i.find(nombre='EMAIL').next_element
=======
def Pagina_aparcamiento_id(request,identificador):
    try:
        aparcamiento = Aparcamiento.objects.get(id=identificador)
        print (aparcamiento.district)
    except Aparcamiento.DoesNotExist:
            context={'name': ""}
            return render_to_response('page_aparcamiento_id.html',context);
    listimages = Image.objects.filter(h_id = aparcamiento.id)
    listcoms=""
    if request.method =='POST':
        value = request.POST.get('comentarios', "")

        n= aparcamiento.numbercom+1;
        aparcamiento.numbercom=n
        aparcamiento.save()
        comment=Comment(h_id=aparcamiento.id,com=aparcamiento,text=value)
        comment.save()
    listcoms=Comment.objects.filter(hid=aparcamiento.id)

    try:
        us=PagUser.objects.get(user=request.user.username)
    except PagUser.DoesNotExist:
        context = {'lista':listimages[0:5],'condicion':"",'url':aparcamiento.url,'name':aparcamiento.name,'address':aparcamiento.address,'body':aparcamiento.body,'comentarios':listcoms,'type':aparcamiento.tipo,'pathf':pathf,'pathi':pathi,'id':ide,'email':aparcamiento.email,
                    'phone':aparcamiento.phone}
        return render_to_response('aparcamiento_id.html', context,context_instance = RequestContext(request))
    context = {'lista':listimages[0:5],'condicion':"",'url':aparcamiento.url,'name':aparcamiento.name,'address':aparcamiento.address,'body':aparcamiento.body,'comentarios':listcoms,'type':aparcamiento.tipo,'pathf':pathf,'pathi':pathi,'id':ide,'email':aparcamiento.email,
                'phone':aparcamiento.phone,'color':us.color,'size':us.size}
    return render_to_response('aparcamiento_id.html', context,context_instance = RequestContext(request))
>>>>>>> b7d703f50780df9cd1d5881d9ec5ff883827bc20

        num_comentarios = 0
        aparcam_elementos = Aparcamiento(nombre=name,
                                         entidad=entity,
                                         descripcion=description,
                                         accesibilidad=accesibility,
                                         url=enlace,
                                         clasevial=classvial,
                                         nombrevia=namevia,
                                         codpostal=cod_postal,
                                         numvia=num_via,
                                         barrio=neighborhood,
                                         distrito=district,
                                         latitud=latitude,
                                         longitud=longitude,
                                         telefono=phone,
                                         email=correo,
                                         numcomentarios=num_comentarios)
        aparcam_elementos.save()

@csrf_exempt
def inicio(request):
    refresh_users(request)
    counter = len(Aparcamiento.objects.all())
    if request.method == "GET":
        if counter == 0:
            response = ""
            formulario = "<br>Actualizar...<br>"
            formulario += "<form action='/' method='post'>"
            formulario += "<input type= 'hidden' name='opcion' value='1'>"
            formulario += "<input type= 'submit' value='Send'>"
            formulario += "</form>"
        else:
            formulario = "<br>Aparcamientos Accesibles<br>"
            formulario = "<form action='/' method='post'>"
            formulario += "<input type= 'hidden' name='opcion' value='2'>"
            formulario += "<input type= 'submit' value='Accesibles'>"
            formulario += "</form>"

            response = ""
            lista = Aparcamiento.objects.order_by('-numcomentarios')
            lista_aux = lista[:5]
            for i in lista_aux:
                if i.numcomentarios == 0:
                    break
                else:
                    response += "<br><a href=" + i.url + ">"
                    response += i.nombre + "</a><br>Direccion: "
                    response += i.clasevial + " " + i.nombrevia
                    response += " " + i.numvia + " "
                    response += i.barrio + ", " + i.distrito + " "
                    response += i.codpostal + "<br><a href=aparcamientos/"
                    response += str(i.id) + ">Mas...</a>"

    elif request.method == "POST":
        opcion = request.POST['opcion']
        if opcion == "1":
            parser(request)
            return redirect("/")
        elif opcion == "2":
            response = ""
            formulario = "<form action='/' method='get'>"
            formulario += "<input type= 'submit' value='Atras'>"
            formulario += "</form>"

            response = ""
            lista = Aparcamiento.objects.order_by('-numcomentarios')
            lista = lista.filter(accesibilidad=1)
            lista_aux = lista[:5]
            for i in lista_aux:
                if i.numcomentarios == 0:
                    break
                else:
                    response += "<br><a href=" + i.url + ">"
                    response += i.nombre + "</a><br>Direccion: "
                    response += i.clasevial + " " + i.nombrevia
                    response += " " + i.numvia + " "
                    response += i.barrio + ", " + i.distrito + " "
                    response += i.codpostal + "<br><a href=aparcamientos/"
                    response += str(i.id) + ">Mas...</a>"

    template = get_template("carpeta_plantillas/inicio.html")
    cont = Context({'content': response, 'formulario_logear': formulario_logear(request),
                'lista_usu': lista_users(request), 'filtro': formulario})
    response = template.render(cont)
    return HttpResponse(response)

@csrf_exempt
def pagina_aparcamientos(request):
    if request.method == "GET":
        lista = Aparcamiento.objects.all()
        response = ""
        for i in lista:
            response += "<br>" + i.nombre + " " + "<a href="
            response += str(i.id) + ">Mas informacion</a>"

        lista_distritos = Aparcamiento.objects.order_by()
        lista_distritos = lista_distritos.values_list('distrito', flat=True).distinct()
        formulario = "<br>Mostrar por distrito<br>"
        formulario += "<form action='/aparcamientos/' method='post'>"
        formulario += "<select name='distrito_selecc'>"
        for j in lista_distritos:
            formulario += "<option value='" + j + "'>" + j
            formulario += "</option>"
        formulario += "<input type= 'submit' value='Mostrar'>"
        formulario += "</form>"

    elif request.method == "POST":
        dis_selecc = request.body.decode('utf-8').split("=")[1]
        distrito = " "
        response = ""
        listadist = Aparcamiento.objects.filter(distrito=dis_selecc)
        for i in listadist:
            response += "<br>" + i.nombre + " " + "<a href="
            response += str(i.id) + ">Mas informacion</a>"

        lista_distritos = Aparcamiento.objects.order_by()
        lista_distritos = lista_distritos.values_list('distrito', flat=True).distinct()
        formulario = "<br>Mostrar por distrito<br>"
        formulario += "<form action='/aparcamientos/' method='post'>"
        formulario += "<select name='distrito_selecc'>"
        for j in lista_distritos:
            formulario += "<option value='" + j + "'>" + j
            formulario += "</option>"
        formulario += "<input type= 'submit' value='Mostrar'>"
        formulario += "</form>"
        formulario += "<br>Toda la lista de aparcamientos<br>"
        formulario += "<form action='/aparcamientos/' method='get'>"
        formulario += "<input type= 'submit' value='volver'>"
        formulario += "</form>"
    else:
        response = "Metodo no permitido"

    template = get_template("carpeta_plantillas/all_aparcamientos.html")
    cont = Context({'content': response, 'formulario_logear': formulario_logear(request),
                'filtro': formulario})
    response = template.render(cont)
    return HttpResponse(response)

@csrf_exempt
def pagina_aparcamiento(request, id):
    aparc_objects = Aparcamiento.objects.get(id=id)
    response = aparc_objects.nombre + "<br>Entidad:" + aparc_objects.entidad
    response += "<br>Descripcion: " + aparc_objects.descripcion
    response += "<br>Accesibilidad: " + str(aparc_objects.accesibilidad)
    response += "<br>Clase via: " + aparc_objects.clasevial + " " + aparc_objects.nombrevia
    response += " " + aparc_objects.numvia + " " + aparc_objects.barrio + ", "
    response += aparc_objects.distrito + "<br>Codigo Postal: " + aparc_objects.codpostal
    response += "<br>Latitud: " + aparc_objects.latitud + " Longitud: "
    response += aparc_objects.longitud + "<br>Telefono: " + aparc_objects.telefono
    response += " Correo: " + aparc_objects.email + "<br><a href=" + aparc_objects.url
    response += ">Aparcamiento Comunid. de Madrid</a>"

    comment_list = Comentario.objects.filter(aparcamiento_comentado=aparc_objects.entidad)
    comment_list = comment_list.order_by('-date')
    response += "<br>Comentarios sobre el aparcamiento:"
    for i in comment_list:
        response += "<br>" + str(i.date) + ": " + i.text

    if request.method == "GET":
        formulario = ""
        formulario_aux = ""
        if request.user.is_authenticated():

            formulario_aux += "<br>Pon un comentario al aparcamiento: "
            formulario_aux += "<form action='/aparcamientos/" + str(id) + "' method="
            formulario_aux += "'post'>Comentario: <input type= 'text' name='texto'>"
            formulario_aux += "<input type= 'hidden' name='opcion' value='1'>"
            formulario_aux += "<input type= 'submit' value='Comentar'>"
            formulario_aux += "</form>"

            formulario += "<br>Guardar en tu pagina este aparcamiento:"
            formulario += "<form action='/aparcamientos/" + str(id)
            formulario += "'method='post'><input type= 'hidden' name='opcion'"
            formulario += "value='2'><input type= 'submit' value='Guardar'>"
            formulario += "</form>"

    elif request.method == "POST":
        aux = request.POST['opcion']
        if aux == "1":
            text = request.POST['texto']
            objecto_comment = Comentario(text=text, aparcamiento_comentado=aparc_objects.entidad)
            objecto_comment.save()

            aparc_objects.numcomentarios = aparc_objects.numcomentarios + 1
            aparc_objects.save()
            URl = "http://localhost:1234/aparcamientos/" + str(id)
            return redirect(URl)

        elif aux == "2":
            pag = Page_user.objects.get(usuario=request.user.username)
            pag.Aparc_Selec.add(aparc_objects)
            pag.save()

            URl = "http://localhost:1234/" + request.user.username
            return redirect(URl)

        else:
            respuesta = "Metodo no permitido"
    else:
        response = "Metodo no permitido"

    template = get_template("carpeta_plantillas/page_aparcamiento.html")
    cont = Context({'content': response, 'formulario_logear': formulario_logear(request),
                'filtro': formulario, 'formulario': formulario_aux})
    response = template.render(cont)
    return HttpResponse(response)

@csrf_exempt
def page_usu(request, nombre_user):
    pag = Page_user.objects.get(usuario=nombre_user)
    titulo = pag.titulo
    formulario = ""
    response = ""
    if request.method == "GET":
        lista = pag.Aparc_Selec.all()
        lengh_lista = len(lista)
        a = lengh_lista/5
        a = math.ceil(a)
        key = request.GET.get("ok", False)
        if key is False:
            if a <= 1:
                for i in lista:
                    response += "<br>" + i.nombre + " "
                    response += "<a href=aparcamientos/" + str(i.id)
                    response += ">Mas informacion</a>"
            else:
                lista = lista[:5]
                for i in lista:
                    response += "<br>" + i.nombre + " "
                    response += "<a href=aparcamientos/" + str(i.id)
                    response += ">Mas informacion</a>"
                for n in range(a):
                    response += "<form action='" + nombre_user + "'method='get'"
                    response += "><input type= 'hidden' name='ok' value='"
                    response += str(n) + "'><input type= 'submit'"
                    response += " value='Otros " + str(n) + "'></form>"
        else:
            contad = request.GET['ok']
            contad = int(contad)
            lengh_1 = contad * 5
            lengh_2 = (contad + 1) * 5
            list_page = lista[lengh_1:lengh_2]
            for i in list_page:
                response += "<br>" + i.nombre + " "
                response += "<a href=aparcamientos/" + str(i.id)
                response += ">Mas informacion</a>"
            for n in range(a):
                response += "<form action='" + nombre_user + "' method='get'>"
                response += "<input type= 'hidden' name='ok' value='" + str(n)
                response += "'><input type= 'submit' value='Otros " + str(i)
                response += "'></form>"

        if nombre_user == request.user.username:
            formulario = "<br>Aqui modificas el titulo de la pagina del usuario:"
            formulario += "<form action='" + nombre_user + "' method='post'>"
            formulario += "Titulo: <input type= 'text' name='titulo'>"
            formulario += "<input type= 'hidden' name='opcion' value='1'>"
            formulario += "<input type= 'submit' value='Cambiar'>"
            formulario += "</form>"

            formulario += "<br>Aqui modificas el color de la pagina del usuario:"
            formulario += "<form action='" + nombre_user + "' method='post'>"
            formulario += "color: <input type= 'text' name='color'>"
            formulario += "<input type= 'hidden' name='opcion' value='2'>"
            formulario += "<input type= 'submit' value='Cambiar'>"
            formulario += "</form>"

            formulario += "<br>Aqui modificas el tamaño de la pagina del usuario:"
            formulario += "<form action='" + nombre_user + "' method='post'>"
            formulario += "Tamaño: <input type= 'text' name='size'>"
            formulario += "<input type= 'hidden' name='opcion' value='3'>"
            formulario += "<input type= 'submit' value='Cambiar'>"
            formulario += "</form>"

    elif request.method == "POST":
        aux = request.POST['opcion']
        response = ""
        if aux == "1":
            aux_titulo = request.POST['titulo']
            pag = Page_user.objects.get(usuario=nombre_user)
            pag.titulo = aux_titulo
            pag.save()

        elif aux == "2":
            aux_color = request.POST['color']
            pag = Page_user.objects.get(usuario=nombre_user)
            pag.background = aux_color
            pag.save()

        elif aux == "3":
            aux_size = request.POST['size']
            pag = Page_user.objects.get(usuario=nombre_user)
            pag.size = aux_size
            pag.save()

        else:
            response = "Metodo no permitido"

        URl = "http://localhost:1234/" + nombre_user
        return redirect(URl)

    else:
        response = "Metodo no permitido"

    template = get_template("carpeta_plantillas/page_usu.html")
    cont = Context({'title': titulo, 'content': response,
                'formulario_logear': formulario_logear(request), 'formulario': formulario})
    response = template.render(cont)
    return HttpResponse(response)

def about(request):
    response = "<h1>RECURSOS DE LA PAGINA:</h1>"
    response += "<p>\"/\" ---> Pagina pricipal de la practica.</p>"
    response += "<p>\"/usuario\" ---> Pagina personal de un usuario.</p>"
    response += "<p>\"/aparcamientos\" ---> Pagina con todos los aparcamientos.</p>"
    response += "<p>\"/aparcamiento\" ---> Pagina de un aparcamiento concreto.</p>"
    response += "<p>\"/xml\" ---> Canal XML del sitio.</p>"
    response += "<p>\"/about\" ---> Pagina con informacion de la practica.</p>"

    response += "<h1>DESCRIPCION GENERAL DE LA PRACTICA:</h1>"
    response += "<p>1. En primer lugar, la aplicacion incluye en su base de datos"
    response += "los aparcamientos de la ciudad de Madrid. Hemos añadido una serie de"
    response += "usuarios, los cuales, si estan registrados, escribiran comentarios en"
    response += "la seccion de TODOS (que muestra los aparcamientos) y podran hacerlo"
    response += "seleccionando un aparcamiento concreto desde sus paginas personales.</p>"
    response += "<p>2. Cada usuario, si esta registrado, como se ha comentado antes,"
    response += "podra cambiar el color del fondo, el tamaño de la letra y cambiar el titulo"
    response += "a su pagina personal, que aparece como Pagina de (mas el nombre que se le da).</p>"
    response += "<p>3. En la seccion de TODOS, aparecen todos los aparcamientos donde se podra"
    response += "filtrar por el distrito al que pertenecen dichos aparcamientos.</p>"

    response += "<h1>AUTORIA:</h1>"
    response += "<p>Borja Egea Madrid</p>"

    template = get_template("carpeta_plantillas/about.html")
    cont = Context({'content': response, 'formulario_logear': formulario_logear(request)})
    response = template.render(cont)
    return HttpResponse(response)

def xml_inicio(request, name_usu):
    response = "<contenidos><infoDataset><nombre>Aparcamientos</nombre>"
    response += "<descripcion>Aparcamientos"
    response += " del usuario: " + name_usu
    response += "</descripcion></infoDataset>"
    pag = Page_user.objects.get(usuario=name_usu)
    lista = pag.Aparc_Selec.all()
    for i in lista:
        response += "<contenido>"
        response += "<nombre>" + i.nombre.replace("&", "&amp;")
        response += "</nombre><Id-Entidad>" + i.entidad
        response += "</Id-Entidad><Descripcion>"
        response += i.descripcion.replace("&", "&amp;")
        response += "</Descripcion><Accesibilidad>"
        response += str(i.accesibilidad) + "</Accesibilidad><Enlace>"
        response += i.url.replace("&", "&amp;") + "</Enlace>"
        response += "<Direccion><Nombre_Via>"
        response += i.nombrevia.replace("&", "&amp;")
        response += "</Nombre_Via><Numero_Via>" + i.numvia
        response += "</Numero_Via><Barrio>" + i.barrio + "</Barrio>"
        response += "<Distrito>" + i.distrito + "</Distrito>"
        response += "</Direccion><Longitud>" + i.longitud
        response += "</Longitud><Latitud>" + i.latitud
        response += "</Latitud></contenido>"

    response += "</contenidos>"
    return HttpResponse(response, content_type="text/xml")

def css(request, nombre_css):
    if request.user.is_authenticated():
        pag = Page_user.objects.get(usuario=request.user.get_username())
        color = pag.background
        size = pag.size
    else:
        color = "white"
        size = "100%"
    template = get_template("carpeta_plantillas/style.css")
    cont = Context({'size': size, 'color': color})
    response = template.render(cont)
    return HttpResponse(response, content_type="text/css")
