from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def inicio(request):
    if request.user.is_authenticated:
        # if request.user.is_superuser:
        #     return redirect('interfaz_admin')
        # else:
        return redirect('interfaz')
    else:
        if request.method == 'POST':
            documento = request.POST.get('documento')
            password = request.POST.get('password')

            user = authenticate(request, documento = documento, password = password)

            if user is not None:
                login(request, user)
                # if request.user.is_superuser:
                # return redirect('interfaz_admin')
                # else:
                return redirect('interfaz')
            elif documento == "" and password == "":
                messages.warning(request, 'Digita en los campos correspondientes para el inicio de sesion')
            else:
                messages.error(request, 'Numero de documento y/o contraseña incorrectos, vuelve a intentarlo')
    return render(request, 'inicio_sesion/inicio.html')


def registrarse(request):
    # * rol = request.POST.get('rol
    # * initial={'rol: 'rol}
    registro = UsuarioForm()# *initial=initial
    if request.method == 'POST':
        # * contraseña = request.POST.get("contraseña")
        registro = UsuarioForm(request.POST, request.FILES)
        
        if registro.is_valid():
            registro.is_active = 1
            registro.save()
            messages.success(request,'Te has registrado exitosamente')
            return redirect('inicio')
        
    return render(request, 'inicio_sesion/registrarse.html', {
        'form': registro
    })

def logout_usuario(request):
    logout(request)
    return redirect('inicio')

class contrasena(LoginRequiredMixin, View):
    template_name = 'usuarios/cambioPswrd/password.html'
    form_class = cambioPasswordForm
    success_url = reverse_lazy('interfaz')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = Usuario.objects.filter(id = request.user.id)
            if user.exists():
                user = user.first()
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                logout(request)
                return redirect(self.success_url)
            return redirect(self.success_url)
        else:
            form = self.form_class(request.POST)
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, self.template_name, {'form': form})
            

def interfaz(request):
    return render(request, 'interfaz/interfaces.html')

def interfaz_admin(request):
    return render(request, 'interfaz_admin/interfaz_admin.html')


# ! Modulo de alimentacion
class Alimentacionn(View):
    model = Alimentacion
    template_name = 'alimentacion/alimentacion.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["alimentacion"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearAlimentacion(CreateView):
    model = Alimentacion
    template_name = 'alimentacion/crear.html'
    form_class = AlimentacionForm
    success_url = reverse_lazy('alimentacion')

class editarAlimentacion(UpdateView):
    model = Alimentacion
    template_name = 'alimentacion/editar.html'
    form_class = AlimentacionForm
    success_url = reverse_lazy('alimentacion')

class confirmarEliminarAlimentacion(DeleteView):
    model = Alimentacion
    template_name = 'alimentacion/alimentacion_confirm_delete.html'
    success_url = reverse_lazy('alimentacion')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarAlimentacion(request, id):
    eliminar = Alimentacion.objects.get(id = id)
    eliminar.delete()
    return redirect('alimentacion')
# ! Modulo de alimentacion


# ! Modulo de detalle de jornada
class DetalleJornadaa(View):
    model = DetalleJornada
    template_name = 'detalle_jornada/detalle_jornada.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["detalle_jornada"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearDetalle(CreateView):
    model = DetalleJornada
    template_name = 'detalle_jornada/crear.html'
    form_class = DetalleJornadaForm
    success_url = reverse_lazy('detalle_jornada')

class editarDetalle(UpdateView):
    model = DetalleJornada
    template_name = 'detalle_jornada/editar.html'
    form_class = DetalleJornadaForm
    success_url = reverse_lazy('detalle_jornada')

class confirmarEliminarDetalle(DeleteView):
    model = DetalleJornada
    template_name = 'detalle_jornada/detalle_jornada_confirm_delete.html'
    success_url = reverse_lazy('detalle_jornada')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarDetalle(request, id):
    eliminar = DetalleJornada.objects.get(id = id)
    eliminar.delete()
    return redirect('detalle_jornada')
# ! Modulo de detalle de jornada

# ! Modulo de estados
class Estadoss(View):
    model = Estados
    template_name = 'estados/estados.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["estados"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearEstado(CreateView):
    model = Estados
    template_name = 'estados/crear.html'
    form_class = EstadosForm
    success_url = reverse_lazy('estados')

class editarEstado(UpdateView):
    model = Estados
    template_name = 'estados/editar.html'
    form_class = EstadosForm
    success_url = reverse_lazy('estados')

class confirmarEliminarEstado(DeleteView):
    model = Estados
    template_name = 'estados/estados_confirm_delete.html'
    success_url = reverse_lazy('estados')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarEstado(request, estado):
    eliminar = Estados.objects.get(estado = estado)
    eliminar.delete()
    return redirect('estados')
# ! Modulo de estados


# ! Modulo de fichas
class Fichass(View):
    model = Ficha
    template_name = 'fichas/fichas.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["fichas"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearFicha(CreateView):
    model = Ficha
    template_name = 'fichas/crear.html'
    form_class = FichaForm
    success_url = reverse_lazy('fichas')

class editarFicha(UpdateView):
    model = Ficha
    template_name = 'fichas/editar.html'
    form_class = FichaForm
    success_url = reverse_lazy('fichas')

class confirmarEliminarFicha(DeleteView):
    model = Ficha
    template_name = 'fichas/fichas_confirm_delete.html'
    success_url = reverse_lazy('fichas')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarFicha(request, id_ficha):
    eliminar = Ficha.objects.get(id_ficha = id_ficha)
    eliminar.delete()
    return redirect('fichas')
# ! Modulo de fichas


# ! Modulo de gallinas
class Gallinass(View):
    model = Gallinas
    template_name = 'gallinas/gallinas.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["gallinas"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearGallinas(CreateView):
    model = Gallinas
    template_name = 'gallinas/crear.html'
    form_class = GallinasForm
    success_url = reverse_lazy('gallinas')

class editarGallinas(UpdateView):
    model = Gallinas
    template_name = 'gallinas/editar.html'
    form_class = GallinasForm
    success_url = reverse_lazy('gallinas')

class confirmarEliminarGallinas(DeleteView):
    model = Gallinas
    template_name = 'gallinas/gallinas_confirm_delete.html'
    success_url = reverse_lazy('gallinas')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarGallinas(request, id):
    eliminar = Gallinas.objects.get(id = id)
    eliminar.delete()
    return redirect('gallinas')
# ! Modulo de gallinas


# ! Modulo de galpones
class Galponess(View):
    model = Galpones
    template_name = 'galpones/galpones.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["galpones"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearGalpon(CreateView):
    model = Galpones
    template_name = 'galpones/crear.html'
    form_class = GalponesForm
    success_url = reverse_lazy('galpones')

class editarGalpon(UpdateView):
    model = Galpones
    template_name = 'galpones/editar.html'
    form_class = GalponesForm
    success_url = reverse_lazy('galpones')

class confirmarEliminarGalpon(DeleteView):
    model = Galpones
    template_name = 'galpones/galpones_confirm_delete.html'
    success_url = reverse_lazy('galpones')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarGalpon(request, id):
    eliminar = Galpones.objects.get(id = id)
    eliminar.delete()
    return redirect('galpones')
# ! Modulo de galpones


# ! Modulo de jornadas
class Jornadass(View):
    model = Jornada
    template_name = 'jornadas/jornadas.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["jornadas"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearJornada(CreateView):
    model = Jornada
    template_name = 'jornadas/crear.html'
    form_class = JornadaForm
    success_url = reverse_lazy('jornadas')

class editarJornada(UpdateView):
    model = Jornada
    template_name = 'jornadas/editar.html'
    form_class = JornadaForm
    success_url = reverse_lazy('jornadas')

class confirmarEliminarJornada(DeleteView):
    model = Jornada
    template_name = 'jornadas/jornadas_confirm_delete.html'
    success_url = reverse_lazy('jornadas')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarJornada(request, id):
    eliminar = Jornada.objects.get(id = id)
    eliminar.delete()
    return redirect('jornadas')
# ! Modulo de jornadas


# ! Modulo de lineas
class Lineass(View):
    model = Linea
    template_name = 'lineas/lineas.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["lineas"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearLinea(CreateView):
    model = Linea
    template_name = 'lineas/crear.html'
    form_class = LineaForm
    success_url = reverse_lazy('lineas')

class editarLinea(UpdateView):
    model = Linea
    template_name = 'lineas/editar.html'
    form_class = LineaForm
    success_url = reverse_lazy('lineas')

class confirmarEliminarLinea(DeleteView):
    model = Linea
    template_name = 'lineas/lineas_confirm_delete.html'
    success_url = reverse_lazy('lineas')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarLinea(request, id):
    eliminar = Linea.objects.get(id = id)
    eliminar.delete()
    return redirect('lineas')
# ! Modulo de lineas


# ! Modulo de mortalidad y descarte
class Mortalidadd(View):
    model = MortalidadDescarte
    template_name = 'mortalidad_descarte/mortalidad_descarte.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["mortalidad_descarte"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearMortalidad(CreateView):
    model = MortalidadDescarte
    template_name = 'mortalidad_descarte/crear.html'
    form_class = MortalidadDescarteForm
    success_url = reverse_lazy('mortalidad_descarte')

class editarMortalidad(UpdateView):
    model = MortalidadDescarte
    template_name = 'mortalidad_descarte/editar.html'
    form_class = MortalidadDescarteForm
    success_url = reverse_lazy('mortalidad_descarte')

class confirmarEliminarMortalidad(DeleteView):
    model = MortalidadDescarte
    template_name = 'mortalidad_descarte/mortalidad_confirm_delete.html'
    success_url = reverse_lazy('mortalidad_descarte')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarMortalidad(request, id):
    eliminar = MortalidadDescarte.objects.get(id = id)
    eliminar.delete()
    return redirect('mortalidad_descarte')
# ! Modulo de mortalidad y descarte

# ! Modulo de produccion diaria
class ProduccionDiariaa(View):
    model = ProduccionDiaria
    template_name = 'prod_diaria/prod_diaria.html'

    def get_queryset(self):
        query = self.model.objects.all()
        return query

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["produccion_diaria"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearProdDiaria(LoginRequiredMixin, CreateView):
    model = ProduccionDiaria
    template_name = 'prod_diaria/crear.html'
    form_class = ProduccionDiariaForm
    success_url = reverse_lazy('produccion_diaria')

    # se crea el metodo From_valid para poder asignar automaticamente el usuario actual al campo 'id_usuario'
    # modificacion -> y se excluye el campo 'id_usurio' en forms.py 
    def form_valid(self, form):
        form.instance.id_usuario = self.request.user  # Asignar el usuario actual al campo id_usuario
        return super().form_valid(form)
    
    
    # def get_context_data(self, **kwargs):
    #     contexto = {}
    #     contexto['form'] = self.form_class
    #     contexto['tipos_huevos'] = TiposHuevos.objects.values_list('id', 'tipos_huevos')
    #     return contexto

class editarProdDiaria(UpdateView):
    model = ProduccionDiaria
    template_name = 'prod_diaria/editar.html'
    form_class = ProduccionDiariaForm
    success_url = reverse_lazy('produccion_diaria')


    # def get_context_data(self, **kwargs):
    #     contexto = {}
    #     contexto['form'] = self.form_class
    #     contexto['tipos_huevos'] = TiposHuevos.objects.values_list('id', 'tipos_huevos')
    #     contexto['object'] = self.get_object()
    #     return contexto

class confirmarEliminarProdDiaria(DeleteView):
    model = ProduccionDiaria
    template_name = 'prod_diaria/prod_diaria_confirm_delete.html'
    success_url = reverse_lazy('produccion_diaria')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarProdDiaria(request, id):
    eliminar = ProduccionDiaria.objects.get(id = id)
    eliminar.delete()
    return redirect('produccion_diaria')
# ! Modulo de produccion diaria


# ! Modulo de rol
class Roll(View):
    model = Rol
    template_name = 'rol/rol.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["rol"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearRol(CreateView):
    model = Rol
    template_name = 'rol/crear.html'
    form_class = RolForm
    success_url = reverse_lazy('rol')

class editarRol(UpdateView):
    model = Rol
    template_name = 'rol/editar.html'
    form_class = RolForm
    success_url = reverse_lazy('rol')

class confirmarEliminarRol(DeleteView):
    model = Rol
    template_name = 'rol/rol_confirm_delete.html'
    success_url = reverse_lazy('rol')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarRol(request, id):
    eliminar = Rol.objects.get(id = id)
    eliminar.delete()
    return redirect('rol')
# ! Modulo de rol


# ! Modulo de tipo de documento
class TipoDocc(View):
    model = TipoDoc
    template_name = 'tipo_doc/tipo_doc.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["tipo_doc"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data()) 

class crearTipoDoc(CreateView):
    model = TipoDoc
    template_name = 'tipo_doc/crear.html'
    form_class = TipoDocForm
    success_url = reverse_lazy('tipo_doc')

class editarTipoDoc(UpdateView):
    model = TipoDoc
    template_name = 'tipo_doc/editar.html'
    form_class = TipoDocForm
    success_url = reverse_lazy('tipo_doc')

class confirmarEliminarTipoDoc(DeleteView):
    model = TipoDoc
    template_name = 'tipo_doc/tipo_doc_confirm_delete.html'
    success_url = reverse_lazy('tipo_doc')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarTipoDoc(request, id):
    eliminar = TipoDoc.objects.get(id = id)
    eliminar.delete()
    return redirect('tipo_doc')
# ! Modulo de tipo de documento


# ! Modulo de tipos de huevos
class TiposHuevoss(View):
    model = TiposHuevos
    template_name = 'tipos_huevos/tipos_huevos.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["tipos_huevos"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class crearTipoHuevo(CreateView):
    model = TiposHuevos
    template_name = 'tipos_huevos/crear.html'
    form_class = TiposHuevosForm
    success_url = reverse_lazy('tipos_huevos')

class editarTipoHuevo(UpdateView):
    model = TiposHuevos
    template_name = 'tipos_huevos/editar.html'
    form_class = TiposHuevosForm
    success_url = reverse_lazy('tipos_huevos')

class confirmarEliminarTipoHuevo(DeleteView):
    model = TiposHuevos
    template_name = 'tipos_huevos/tipos_huevos_confirm_delete.html'
    success_url = reverse_lazy('tipos_huevos')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarTipoHuevo(request, id):
    eliminar = TiposHuevos.objects.get(id = id)
    eliminar.delete()
    return redirect('tipos_huevos')
# ! Modulo de tipos de huevos


# ! Modulo de usuario
class Usuarioss(View):
    model = Usuario
    template_name = 'usuarios/usuarios.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["usuarios"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class crearUsuario(CreateView):
    model = Usuario
    template_name = 'usuarios/crear.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios')

class EditarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuarios/editar.html'
    form_class = UsuarioForm2
    success_url = reverse_lazy('usuarios')

class confirmarEliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuarios_confirm_delete.html'
    success_url = reverse_lazy('usuarios')

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

def eliminarUsuario(request, id):
    eliminar = Usuario.objects.get(id = id)
    eliminar.delete()
    return redirect('usuarios')
# ! Modulo de usuario