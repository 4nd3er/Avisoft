from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def inicio(request):
    return render(request, 'inicio_sesion/inicio.html')

def registrarse(request):
    return render(request, 'inicio_sesion/registrarse.html')

def contrasena(request):
    return render(request, 'inicio_sesion/contrasena.html')

def interfaz(request):
    return render(request, 'interfaz/interfaz.html')

def interfaz_admin(request):
    return render(request, 'interfaz_admin/interfaz_admin.html')

# ! Modulo de galpones
def galpones(request):
    datosg = Galpones.objects.all()
    return render(request, 'galpones/galpones.html', {'datosg': datosg})

def crear_galpones(request):
    form = GalponesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('galpones')
    return render(request, 'galpones/crear.html', {'form':form})

def editar_galpones(request, id):
    datosg = Galpones.objects.get(id=id)
    form = GalponesForm(request.POST or None, instance=datosg)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('galpones')
    return render(request, 'galpones/editar.html', {'form':form})
    
def eliminar_galpon(request, id):
    datoseli = Galpones.objects.get(id=id)
    datoseli.delete()
    return redirect('galpones')
# ! Modulo de galpones


# ! Modulo de gallinas
def gallinas(request):
    gallinas = Gallinas.objects.all()
    return render(request, 'gallinas/gallinas.html', {'gallinas': gallinas})

def crear_gallinas(request):
    formulario = GallinasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('gallinas')
    return render(request, 'gallinas/crear.html', {'formulario': formulario})

def editar_gallinas(request, id):
    gallinas = Gallinas.objects.get(id=id)
    formulario = GallinasForm(request.POST or None, request.FILES or None, instance=gallinas)
    return render(request, 'gallinas/editar.html', {'formulario': formulario})

def eliminar_gallinas(request, id):
    gallinas = Gallinas.objects.get(id=id)
    gallinas.delete()
    return redirect('gallinas')
# ! Modulo de gallinas


# ! Modulo de produccion diaria
def prod_diaria(request):
    producciones_diarias = ProduccionDiaria.objects.all()
    return render(request, 'prod_diaria/prod_diaria.html', {'producciones_diarias' : producciones_diarias})

def crear_prod_diaria(request):
    tipos_huevos = TiposHuevos.objects.values_list('id', 'tipos_huevos')
    formulario = ProduccionDiariaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('prod_diaria')
    return render(request, 'prod_diaria/crear_prod_diaria.html', {'formulario': formulario, 'tipos_huevos' : tipos_huevos})

def editar_prod_diaria(request, id):
    tipos_huevos = TiposHuevos.objects.values_list('id', 'tipos_huevos')
    produccion_diaria = ProduccionDiaria.objects.get(id = id)
    formulario = ProduccionDiariaForm(request.POST or None, instance = produccion_diaria)
    if formulario.is_valid():
        formulario.save()
        return redirect('prod_diaria')
    return render(request, 'prod_diaria/editar_prod_diaria.html', {'formulario': formulario, 'tipos_huevos' : tipos_huevos})

def eliminar_prod_diaria(request, id):
    produccion_diaria = ProduccionDiaria.objects.get(id = id)
    produccion_diaria.delete()
    return redirect('prod_diaria')
# ! Modulo de produccion diaria


# ! Modulo de alimentacion
def alimentacion(request):
    datos_alimentacion = Alimentacion.objects.all()
    return render(request, 'alimentacion/alimentacion.html', {'datos_alimentacion': datos_alimentacion})

def registrar_alimentacion(request):
    form = AlimentacionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('alimentacion')
    return render(request, 'alimentacion/registroali.html', {'form': form})

def editar_alimentacion(request, id):
    datoa = Alimentacion.objects.get(id=id)
    form = AlimentacionForm(request.POST or None, instance=datoa)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('alimentacion')
    return render(request, 'alimentacion/aleditar.html', {'form': form})

def eliminar_alimentacion(request, id):
    datosa = Alimentacion.objects.get(id=id)
    datosa.delete()
    return redirect('alimentacion')
# ! Modulo de alimentacion


# ! Modulo de mortalidad
def mortalidad(request):
    datos_mortalidad = MortalidadDescarte.objects.all()
    return render(request, 'mortalidad/mortalidad.html', {'datos_mortalidad': datos_mortalidad})

def registrar_mortalidad(request):
    form = MortalidadDescarteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mortalidad')
    return render(request, 'mortalidad/mregistrar.html', {'form': form})

def editar_mortalidad(request, id):
    datosme = MortalidadDescarte.objects.get(id=id)
    form = MortalidadDescarteForm(request.POST or None, instance=datosme)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('mortalidad')
    return render(request, 'mortalidad/meditar.html', {'form': form})

def eliminar_mortalidad(request, id):
    datosm = MortalidadDescarte.objects.get(id=id)
    datosm.delete()
    return redirect('mortalidad')
# ! Modulo de mortalitad

def registro_diario(request):
    return render(request, 'registro_diario/registro_diario.html')


# ! Modulo de estados
def estados(request):
    estados = Estados.objects.all()
    return render(request, 'estados/estados.html', {"estados": estados})

def registro(request):
    ultimo_estado = Estados.objects.latest('estado')
    formulario = EstadosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        estado_nuevo = formulario.save(commit=False)
        estado_nuevo.estado = ultimo_estado.estado + 1
        estado_nuevo.save()
        return redirect('estados')
    return render(request,'estados/registro.html', {'formulario': formulario})

def editar_estado(request, estado):
    estado_editar = Estados.objects.get(estado=estado)
    formulario = EstadosForm(request.POST or None, request.FILES or None, instance=estado_editar)
    if formulario.is_valid():
        formulario.save()
        return redirect('estados')
    return render(request, 'estados/editar.html', {'formulario': formulario})

def eliminar_estado(request, estado):
    estado_eliminar = get_object_or_404(Estados, estado=estado)
    estado_eliminar.delete()
    return redirect('estados')
# ! Modulo de estados


# ! Modulo de fichas
def ficha(request):
    ficha = Ficha.objects.all()
    return render(request, 'ficha/ficha.html', {"ficha": ficha})

def crear_ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ficha')
        else:
            # Agregar este código para mostrar errores de validación
            print(form.errors)
    else:
        form = FichaForm()
    estados = Estados.objects.all()
    return render(request, 'ficha/crear_ficha.html', {'form': form, 'estados': estados})

def editar_ficha(request, id_ficha):
    ficha = get_object_or_404(Ficha, id_ficha=id_ficha)
    form = FichaForm(request.POST or None, instance=ficha)
    if form.is_valid():
        form.save()
        return redirect('ficha')
    estados = Estados.objects.all()
    return render(request, 'ficha/editar_ficha.html', {'form': form, 'ficha': ficha, 'estados': estados})

def eliminar_ficha(request, id_ficha):
    ficha = get_object_or_404(Ficha, pk=id_ficha)
    ficha.delete()
    return redirect('ficha')
# ! Modulo de fichas


# ! Modulo de jornada
def jornada(request):
    datos_jornada=Jornada.objects.all()
    return render(request, 'jornada/jornada.html', {'datos_jornada': datos_jornada})

def crear_jornada(request):
    registrarjornada = JornadaForm(request.POST or None)
    if registrarjornada.is_valid():
        registrarjornada.save()
        return redirect('jornada')
    return render(request, 'jornada/crear_jornada.html', {'registrarjornada': registrarjornada})

def editar_jornada(request, id):   
    datoj = Jornada.objects.get(id=id)
    editarj = JornadaForm(request.POST or None, instance=datoj) 
    if editarj.is_valid() and request.POST:
        editarj.save()
        return redirect('jornada')
    return render(request, 'jornada/editar_jornada.html', {'editarj': editarj})

def eliminar_jornada(request, id):
    datojo = Jornada.objects.get(id=id)
    datojo.delete()    
    return redirect('jornada')
# ! Modulo de jornada

# ! Modulo de detalle de jornada
def detalle_jornada(request):
    datos_detalle = DetalleJornada.objects.all()
    return render(request, 'detalle_jornada/detalle_jornada.html', {'datos_detalle': datos_detalle})

def crear_detalle(request):
    form = DetalleJornadaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('detalle_jornada')
    return render(request, 'detalle_jornada/crear_detalle.html', {'form': form})

def editar_detalle(request, id):   
    datod = DetalleJornada.objects.get(id=id)
    form = DetalleJornadaForm(request.POST or None, instance=datod) 
    if form.is_valid():
        form.save()
        return redirect('detalle_jornada')
    return render(request, 'detalle_jornada/editar_detalle.html', {'form': form})

def eliminar_detalle(request, id):
    datodet = DetalleJornada.objects.get(id=id)
    datodet.delete()    
    return redirect('detalle_jornada')
# ! Modulo de detalle de jornada


# ! Modulo de linea
def linea(request):
    linea = Linea.objects.all()
    return render(request, 'linea/linea.html', {'linea': linea})

def crear_li(request):
    formulario = LineaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('linea')
    return render(request, 'linea/crear_li.html', {'formulario': formulario}) 

def editar_li(request,id):
    linea = Linea.objects.get(id=id)
    formulario = LineaForm(request.POST or None, request.FILES or None, instance=linea)
    if formulario.is_valid():
        formulario.save()
        return redirect('linea')
    return render(request, 'linea/editar_li.html',{'formulario': formulario})

def eliminar_li(request, id):
    linea = Linea.objects.get(id=id)
    linea.delete()
    return redirect('linea')
# ! Modulo de linea


# ! Modulo rol
def rol(request):
    rol = Rol.objects.all()
    return render(request, 'rol/rol.html', {'rol': rol})

def crear_rol(request):
    formulario = RolForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('rol')
    return render(request, 'rol/crear_rol.html', {'formulario': formulario})

def editar_rol(request, id):
    rol = Rol.objects.get(id = id)
    formulario = RolForm(request.POST or None, instance = rol)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('rol')
    return render(request, 'rol/editar_rol.html', {'formulario': formulario})

def eliminar_rol(request, id):
    rol = Rol.objects.get(id = id)
    rol.delete()
    return redirect('rol')
# ! Modulo rol


# ! Modulo de tipos de huevos
def tipos_huevos(request):
    datost = TiposHuevos.objects.all()
    return render(request, 'tipos_huevos/tipos_huevos.html',{'datost': datost})

def crear_thuevos(request):
    formhuevos = TiposHuevosForm(request.POST or None)
    if formhuevos.is_valid():
        formhuevos.save()
        return redirect('tipos_huevos')
    return render(request, 'tipos_huevos/crearthuevos.html', {'formhuevos':formhuevos})

def editar_thuevos(request, id):
    datosh = TiposHuevos.objects.get(id=id)
    editartihue = TiposHuevosForm(request.POST or None, instance=datosh)
    if editartihue.is_valid() and request.POST:
        editartihue.save()
        return redirect('tipos_huevos')
    return render(request, 'tipos_huevos/editarthuevos.html', {'editartihue':editartihue})
    
def eliminar_thuevos(request, id):
    datoseli = TiposHuevos.objects.get(id=id)
    datoseli.delete()
    return redirect('tipos_huevos')
# ! Modulo de tipos de huevos


# ! Modulo de tipos de documentos
def tipo_doc(request):
    doc = TipoDoc.objects.all()
    return render(request, 'tipo_doc/tipo_doc.html', {"doc": doc})

def insertar(request):
    doc = TipoDocForm(request.POST or None)
    if doc.is_valid():
        doc.save()
        return redirect('tipo_doc')
    return render(request,'tipo_doc/insertar.html', {'doc': doc})

def editardoc(request, tipo_doc):
    tipo_doc_obj = get_object_or_404(TipoDoc, tipo_doc=tipo_doc)
    if request.method == 'POST':
        form = TipoDocForm(request.POST, instance=tipo_doc_obj)
        if form.is_valid():
            form.save()
            return redirect('tipo_doc')
    else:
        form = TipoDocForm(instance=tipo_doc_obj)
    return render(request, 'tipo_doc/editardoc.html', {'form': form, 'tipo_doc': tipo_doc_obj})

def eliminar_tipoDoc(request, tipo_doc):
    tipo_doc = get_object_or_404(TipoDoc, tipo_doc=tipo_doc)
    tipo_doc.delete()
    return redirect('tipo_doc')
# ! Modulo de tipos de documentos


# ! Modulo usuario
def usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/usuario.html', {'usuarios': usuarios})

def crear_usuario(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuario')
    return render(request, 'usuario/crear_usuario.html', {'formulario': formulario})

def edit_usuario(request, id):
    usuario = Usuario.objects.get(id = id)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance = usuario)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('usuario')
    return render(request, 'usuario/editar_usuario.html', {'formulario': formulario})

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    return redirect('usuario')
# ! Modulo usuario