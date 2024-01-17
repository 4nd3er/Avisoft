import json
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.core.serializers import serialize
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, ListView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime, timezone
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from localStoragePy import localStoragePy

localStorage = localStoragePy('me.jkelol111.mypythonapp', 'text')
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# ! Modulo de inicio e interfaces
def registrarse(request):
    # * rol = request.POST.get('rol
    # * initial={'rol: 'rol}
    registro = UsuarioForm()# *initial=initial
    if request.method == 'POST':
        # * contraseña = request.POST.get("contraseña")
        registro = UsuarioForm(request.POST, request.FILES)
        
        if registro.is_valid():
            registro.is_active = 1 # TODO comprobar si sirve
            registro.save()
            messages.success(request,'Te has registrado exitosamente')
            return redirect('inicio')
    return render(request, 'inicio_sesion/registrarse.html', { 'form': registro })


def inicio(request):
    if request.user.is_authenticated:
        return redirect('interfaz')
    else:
        if request.method == 'POST':
            documento = request.POST.get('documento')
            password = request.POST.get('password')

            user = authenticate(request, documento = documento, password = password)

            if documento == "" and password == "":
                messages.warning(request, 'Digita en los campos correspondientes para el inicio de sesion')
                return render(request, 'inicio_sesion/inicio.html')
            userFilter = Usuario.objects.filter(documento=documento).values_list('is_active', flat=True)
            if user is not None:
                login(request, user)
                return redirect('interfaz')
            elif not userFilter:
                messages.error(request, 'Usuario no registrado en la pagina web, registrate para iniciar sesion')
            elif not userFilter[0]:
                messages.error(request, 'Usuario bloqueado, comunicate con el administrador')
            else:
                messages.error(request, 'Numero de documento y/o contraseña incorrectos, vuelve a intentarlo')
    return render(request, 'inicio_sesion/inicio.html')


class contrasena(LoginRequiredMixin, ListView):
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


def logout_usuario(request):
    logout(request)
    return redirect('inicio')
# ! Modulo de inicio e interfaces


# ! Modulo de registro diario
class registroDiario(ListView):
    template_name = 'registro_diario/registro_diario.html'
    model = ProduccionDiaria

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['alimentacion'] = Alimentacion.objects.all().order_by('-id')
        contexto['mortalidadDescarte'] = MortalidadDescarte.objects.all().order_by('-id')
        contexto['produccionDiaria'] = self.get_queryset()
        alimentacion_dict = {'alimentacion': contexto['alimentacion']}
        mortalidad_dict = {'mortalidadDescarte': contexto['mortalidadDescarte']}
        produccion_dict = {'produccionDiaria': contexto['produccionDiaria']}
        merged_dict = {}
        merged_dict.update(alimentacion_dict)
        merged_dict.update(mortalidad_dict)
        merged_dict.update(produccion_dict)
        return merged_dict

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'datos': self.get_context_data()})
    
    def post(self, request, *args, **kwargs):
        query = self.get_context_data()
        if query == 0:
            messages.error(request, 'Debes buscar algun dato para generar el reporte')
            return render(request, self.template_name, {'datos': self.get_queryset()})
        else:
            wb = Workbook()
            ws = wb.active
            ws.title = 'Hoja1'

            ws['B2'].alignment = Alignment(horizontal = 'center', vertical = 'center')
            ws['B2'].border = Border(left = Side(border_style = 'thin'), right = Side(border_style = 'thin'),
                                        top = Side(border_style = 'thin'), bottom = Side(border_style = 'thin'))
            ws['B2'].fill = PatternFill(start_color = '39A900', fill_type = 'solid')
            ws['B2'].font = Font(name = 'Arial', size = 15, bold = True, color = 'FFFFFF')
            ws['B2'] = f'REPORTE REGISTRO DIARIO'

            ws.merge_cells('B2:E2')
            listColumn = ['B', 'C', 'D', 'E']
            listName = ['Galpon', 'Alimentación', 'Mortalidad y Descarte', 'Produccion Diaria']
            countName = 0
            count = 3
            ws.row_dimensions[2].height = 25
            for i in listColumn:
                ws.column_dimensions[i].width = 50
                ws[f'{listColumn[countName]}3'].alignment = Alignment(horizontal = 'center', vertical = 'center')
                ws[f'{listColumn[countName]}3'].border = Border(left = Side(border_style = 'thin'), right = Side(border_style = 'thin'),
                                            top = Side(border_style = 'thin'), bottom = Side(border_style = 'thin'))
                ws[f'{listColumn[countName]}3'].fill = PatternFill(start_color = 'FFCE40', fill_type = 'solid')
                ws[f'{listColumn[countName]}3'].font = Font(name = 'Arial', size = 11)
                ws[f'{listColumn[countName]}3'] = listName[countName]
                count += 1
                countName += 1
            
            # Pintamos los datos en el reporte
            listName = ['alimentacion', 'mortalidadDescarte', 'produccionDiaria']
            countColumn = 2
            for i in listName:
                countRow = 4
                for q in query[i]:
                    ws.cell(row = countRow, column = countColumn).alignment = Alignment(horizontal = 'center', vertical = 'center')
                    ws.cell(row = countRow, column = countColumn).border = Border(left = Side(border_style = 'thin'), right = Side(border_style = 'thin'),
                                                    top = Side(border_style = 'thin'), bottom = Side(border_style = 'thin'))
                    ws.cell(row = countRow, column = countColumn).fill = PatternFill(start_color = 'FBFBE2', fill_type = 'solid')
                    ws.cell(row = countRow, column = countColumn).font = Font(name = 'Arial', size = '11')
                    if i == 'produccionDiaria':
                        valueRow = str(getattr(q, 'id_galpon', 'id_galpon'))
                        ws.cell(row=4, column=2).value = valueRow
                        ws.cell(row = countRow, column = 5).alignment = Alignment(horizontal = 'center', vertical = 'center')
                        ws.cell(row = countRow, column = 5).border = Border(left = Side(border_style = 'thin'), right = Side(border_style = 'thin'),
                                                        top = Side(border_style = 'thin'), bottom = Side(border_style = 'thin'))
                        ws.cell(row = countRow, column = 5).fill = PatternFill(start_color = 'FBFBE2', fill_type = 'solid')
                        ws.cell(row = countRow, column = 5).font = Font(name = 'Arial', size = '11')
                        ws.cell(row=countRow, column=5).value = str(q)
                    elif i == 'alimentacion':
                        valueRow = str(getattr(q, 'id_galpon', 'id_galpon'))
                        ws.cell(row=4, column=2).value = valueRow
                        ws.cell(row=countRow, column=3).value = str(q)
                    elif i == 'mortalidadDescarte':
                        valueRow = str(getattr(q, 'id_galpon', 'id_galpon'))
                        ws.cell(row=4, column=2).value = valueRow
                        ws.cell(row=countRow, column=4).value = str(q)
                    else:
                        ws.cell(row=countRow, column=countColumn).value = str(q)
                    countRow += 1
                countColumn += 1

            # Nombre del archivo
            nombreArchivo = f'REPORTE REGISTRO DIARIO.xlsx'
            # Definir el tipo de respuesta
            response = HttpResponse(content_type = 'application/ms-excel')
            contenido = "attachment; filename = {0}".format(nombreArchivo)
            response['Content-Disposition'] = contenido
            wb.save(response)
            return response
        return render(request, self.template_name, {'datos': self.get_queryset()})
# ! Modulo de registro diario


# ! Modulo de alimentacion
class Alimentacionn(ListView):
    model = Alimentacion
    template_name = 'alimentacion/alimentacion.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["alimentacion"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'alimentacion': self.get_queryset()})

class crearAlimentacion(CreateView):
    model = Alimentacion
    template_name = 'alimentacion/crear.html'
    form_class = AlimentacionForm
    success_url = reverse_lazy('alimentacion')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('alimentacion')

class editarAlimentacion(UpdateView):
    model = Alimentacion
    template_name = 'alimentacion/editar.html'
    form_class = AlimentacionForm
    success_url = reverse_lazy('alimentacion')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('alimentacion')

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


# ! Modulo de fichas
class Fichass(ListView):
    model = Ficha
    template_name = 'fichas/fichas.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id_ficha')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["fichas"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id = request.user.id).values_list('is_staff', flat = True)
        if user[0] == True:
            if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
            else:
                return render(request, self.template_name, {'fichas': self.get_queryset()})
        else:
            return redirect('interfaz')

class crearFicha(CreateView):
    model = Ficha
    template_name = 'fichas/crear.html'
    form_class = FichaForm
    success_url = reverse_lazy('fichas')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('fichas')

class editarFicha(UpdateView):
    model = Ficha
    template_name = 'fichas/editar.html'
    form_class = FichaForm
    success_url = reverse_lazy('fichas')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('fichas')

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
class Gallinass(ListView):
    model = Gallinas
    template_name = 'gallinas/gallinas.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["gallinas"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'gallinas': self.get_queryset()})

class crearGallinas(CreateView):
    model = Gallinas
    template_name = 'gallinas/crear.html'
    form_class = GallinasForm
    success_url = reverse_lazy('gallinas')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                nombreGalpon = form.cleaned_data['id_galpon']
                galpon = Galpones.objects.get(nombre_galpon=nombreGalpon)
                cant_gallinas_form = form.cleaned_data['cantidad_gallinas']
                localStorage.setItem('gallinas', cant_gallinas_form)
                galpon.cant_gall += cant_gallinas_form
                galpon.save()
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('gallinas')

class editarGallinas(UpdateView):
    model = Gallinas
    template_name = 'gallinas/editar.html'
    form_class = GallinasForm
    success_url = reverse_lazy('gallinas')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                nombreGalpon = form.cleaned_data['id_galpon'] 
                galpon = Galpones.objects.get(nombre_galpon=nombreGalpon)
                cant_gallinas_form = form.cleaned_data['cantidad_gallinas']
                value = int(localStorage.getItem('gallinas'))
                if value > cant_gallinas_form:
                    value -= cant_gallinas_form
                    galpon.cant_gall -= value
                    localStorage.setItem('gallinas', value)
                else:
                    cant_gallinas_form -= value
                    galpon.cant_gall += cant_gallinas_form
                    localStorage.setItem('gallinas', cant_gallinas_form)
                galpon.save()
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('gallinas')

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
class Galponess(ListView):
    model = Galpones
    template_name = 'galpones/galpones.html'

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")

        if busqueda:
            query = self.model.objects.filter(
                Q(nombre_galpon__icontains = busqueda) |
                Q(area__icontains = busqueda) |
                Q(capac_bebed__icontains = busqueda) |
                Q(cant_bebed__icontains = busqueda) |
                Q(capac_comed__icontains = busqueda) |
                Q(cant_comed__icontains = busqueda) |
                Q(capac_gall__icontains = busqueda) |
                Q(cant_gall__icontains = busqueda) |
                Q(capac_nidales__icontains = busqueda) |
                Q(cant_nidales__icontains = busqueda)
                ).distinct()
        else:
            query = self.model.objects.all().order_by('-id')
        return query

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["galpones"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'galpones': self.get_queryset()})

class crearGalpon(CreateView):
    model = Galpones
    template_name = 'galpones/crear.html'
    form_class = GalponesForm
    success_url = reverse_lazy('galpones')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('galpones')

class editarGalpon(UpdateView):
    model = Galpones
    template_name = 'galpones/editar.html'
    form_class = GalponesForm
    success_url = reverse_lazy('galpones')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('galpones')

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
class Jornadass(ListView):
    model = Jornada
    template_name = 'jornadas/jornadas.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["jornadas"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id = request.user.id).values_list('is_staff', flat = True)
        if user[0] == True:
            if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
            else:
                return render(request, self.template_name, {'jornadas': self.get_queryset()})
        else:
            return redirect('interfaz')

class crearJornada(CreateView):
    model = Jornada
    template_name = 'jornadas/crear.html'
    form_class = JornadaForm
    success_url = reverse_lazy('jornadas')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('jornadas')

class editarJornada(UpdateView):
    model = Jornada
    template_name = 'jornadas/editar.html'
    form_class = JornadaForm
    success_url = reverse_lazy('jornadas')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('jornadas')

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
class Lineass(ListView):
    model = Linea
    template_name = 'lineas/lineas.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["lineas"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id = request.user.id).values_list('is_staff', flat = True)
        if user[0] == True:
            if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
            else:
                return render(request, self.template_name, {'lineas': self.get_queryset()})
        else:
            return redirect('interfaz')

class crearLinea(CreateView):
    model = Linea
    template_name = 'lineas/crear.html'
    form_class = LineaForm
    success_url = reverse_lazy('lineas')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('lineas')

class editarLinea(UpdateView):
    model = Linea
    template_name = 'lineas/editar.html'
    form_class = LineaForm
    success_url = reverse_lazy('lineas')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('lineas')

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
class Mortalidadd(ListView):
    model = MortalidadDescarte
    template_name = 'mortalidad_descarte/mortalidad_descarte.html'

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")

        if busqueda:
            query = self.model.objects.filter(
                Q(id_galpon__nombre_galpon__icontains = busqueda) |
                Q(cant_muertas__icontains = busqueda) |
                Q(cant_descarte__icontains = busqueda) |
                Q(id_tipo_descarte__tipo__icontains = busqueda) |
                Q(saldo__icontains = busqueda)
                ).distinct()
        else:
            query = self.model.objects.all().order_by('-id')
        return query

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["mortalidad_descarte"] = self.get_queryset()
        contexto["data"] = Galpones.objects.all().values_list("id", "cant_gall")
        return contexto
    
    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'mortalidad_descarte': self.get_queryset()})

class crearMortalidad(CreateView):
    model = MortalidadDescarte
    template_name = 'mortalidad_descarte/crear.html'
    form_class = MortalidadDescarteForm
    success_url = reverse_lazy('mortalidad_descarte')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Realizar la consulta a la base de datos
        consulta_resultados = Galpones.objects.all().values_list("id", "cant_gall")

        context['data'] = consulta_resultados

        return context

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('mortalidad_descarte')

class editarMortalidad(UpdateView):
    model = MortalidadDescarte
    template_name = 'mortalidad_descarte/editar.html'
    form_class = MortalidadDescarteForm
    success_url = reverse_lazy('mortalidad_descarte')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('mortalidad_descarte')

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
class ProduccionDiariaa(ListView):
    model = ProduccionDiaria
    template_name = 'prod_diaria/prod_diaria.html'

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")

        if busqueda:
            query = self.model.objects.filter(
                Q(id_galpon__nombre_galpon__icontains = busqueda) |
                Q(id_jornada__jornada__icontains = busqueda) |
                Q(id_tipo_huevo__tipos_huevos = busqueda )|
                Q(id_usuario__nombre__icontains = busqueda) |
                Q(fecha__icontains = busqueda)
                ).distinct().order_by('-id')
        else:
            query = self.model.objects.all().order_by('-id')[:3]
        return query

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["produccion_diaria"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
        else:
            return render(request, self.template_name, {'produccion_diaria': self.get_queryset()})

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
    
    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.instance.id_usuario = self.request.user
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('produccion_diaria')

class editarProdDiaria(UpdateView):
    model = ProduccionDiaria
    template_name = 'prod_diaria/editar.html'
    form_class = ProduccionDiariaForm
    success_url = reverse_lazy('produccion_diaria')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('produccion_diaria')

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
class Roll(ListView):
    model = Rol
    template_name = 'rol/rol.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["rol"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id = request.user.id).values_list('is_staff', flat = True)
        if user[0] == True:
            if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
            else:
                return render(request, self.template_name, {'rol': self.get_queryset()})
        else:
            return redirect('interfaz')

class crearRol(CreateView):
    model = Rol
    template_name = 'rol/crear.html'
    form_class = RolForm
    success_url = reverse_lazy('rol')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('rol')

class editarRol(UpdateView):
    model = Rol
    template_name = 'rol/editar.html'
    form_class = RolForm
    success_url = reverse_lazy('rol')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('rol')

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
class TipoDocc(ListView):
    model = TipoDoc
    template_name = 'tipo_doc/tipo_doc.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["tipo_doc"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id = request.user.id).values_list('is_staff', flat = True)
        if user[0] == True:
            if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
            else:
                return render(request, self.template_name, {'tipo_doc': self.get_queryset()})
        else:
            return redirect('interfaz')

class crearTipoDoc(CreateView):
    model = TipoDoc
    template_name = 'tipo_doc/crear.html'
    form_class = TipoDocForm
    success_url = reverse_lazy('tipo_doc')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('tipo_doc')

class editarTipoDoc(UpdateView):
    model = TipoDoc
    template_name = 'tipo_doc/editar.html'
    form_class = TipoDocForm
    success_url = reverse_lazy('tipo_doc')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('tipo_doc')

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
class TiposHuevoss(ListView):
    model = TiposHuevos
    template_name = 'tipos_huevos/tipos_huevos.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["tipos_huevos"] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id = request.user.id).values_list('is_staff', flat = True)
        if user[0] == True:
            if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_context_data()), 'application/json')
            else:
                return render(request, self.template_name, {'tipos_huevos': self.get_queryset()})
        else:
            return redirect('interfaz')

class crearTipoHuevo(CreateView):
    model = TiposHuevos
    template_name = 'tipos_huevos/crear.html'
    form_class = TiposHuevosForm
    success_url = reverse_lazy('tipos_huevos')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('tipos_huevos')

class editarTipoHuevo(UpdateView):
    model = TiposHuevos
    template_name = 'tipos_huevos/editar.html'
    form_class = TiposHuevosForm
    success_url = reverse_lazy('tipos_huevos')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('tipos_huevos')

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
class Usuarioss(ListView):
    model = Usuario
    template_name = 'usuarios/usuarios.html'

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        if busqueda:
            query = self.model.objects.filter(
                Q(nombre__icontains = busqueda) |
                Q(apellido__icontains = busqueda) |
                Q(id_tipo_doc__tipo_doc__icontains = busqueda) |
                Q(documento__icontains = busqueda) |
                Q(celular__icontains = busqueda) |
                Q(id_ficha__num_ficha__icontains = busqueda) |
                Q(id_rol__tipo_rol__icontains = busqueda) |
                Q(email__icontains = busqueda)
                ).distinct().order_by('-id')
        else:
            query = 0
        return query

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto["usuarios"] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id = request.user.id).values_list('is_staff', flat = True)
        if user[0] == True:
            if is_ajax(request=request):
                return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
            else:
                return render(request, self.template_name, {'usuarios': self.get_queryset()})
        else:
            return redirect('interfaz')

    def post(self, request, *args, **kwargs):
        query = self.get_queryset()
        if query == 0:
            messages.error(request, 'Debes buscar algun dato para generar el reporte')
            return render(request, self.template_name, {'usuarios': self.get_queryset()})
        else:
            wb = Workbook()
            ws = wb.active
            ws.title = 'Hoja1'

            ws['B2'].alignment = Alignment(horizontal = 'center', vertical = 'center')
            ws['B2'].border = Border(left = Side(border_style = 'thin'), right = Side(border_style = 'thin'),
                                        top = Side(border_style = 'thin'), bottom = Side(border_style = 'thin'))
            ws['B2'].fill = PatternFill(start_color = '39A900', fill_type = 'solid')
            ws['B2'].font = Font(name = 'Arial', size = 15, bold = True, color = 'FFFFFF')
            ws['B2'] = f'REPORTE {self.model.__name__.upper()}S'

            ws.merge_cells('B2:K2')
            listColumn = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
            listName = ['Nombre', 'Apellido', 'Tipo de Documento', 'Documento', 'Celular', 'email', 'Ficha', 'Rol', 'Registro', 'Ultima Conexión']
            countName = 0
            count = 3
            ws.row_dimensions[2].height = 25
            for i in listColumn:
                ws.column_dimensions[i].width = 35
                ws[f'{listColumn[countName]}3'].alignment = Alignment(horizontal = 'center', vertical = 'center')
                ws[f'{listColumn[countName]}3'].border = Border(left = Side(border_style = 'thin'), right = Side(border_style = 'thin'),
                                            top = Side(border_style = 'thin'), bottom = Side(border_style = 'thin'))
                ws[f'{listColumn[countName]}3'].fill = PatternFill(start_color = 'FFCE40', fill_type = 'solid')
                ws[f'{listColumn[countName]}3'].font = Font(name = 'Arial', size = 11)
                ws[f'{listColumn[countName]}3'] = listName[countName]
                count += 1
                countName += 1
            
            # Pintamos los datos en el reporte
            listName = ['nombre', 'apellido', 'id_tipo_doc', 'documento' , 'celular', 'email', 'id_ficha', 'id_rol', 'registro', 'last_login']
            countColumn = 2
            for i in listName:
                countRow = 4
                for q in query:
                    ws.cell(row = countRow, column = countColumn).alignment = Alignment(horizontal = 'center', vertical = 'center')
                    ws.cell(row = countRow, column = countColumn).border = Border(left = Side(border_style = 'thin'), right = Side(border_style = 'thin'),
                                                    top = Side(border_style = 'thin'), bottom = Side(border_style = 'thin'))
                    ws.cell(row = countRow, column = countColumn).fill = PatternFill(start_color = 'FBFBE2', fill_type = 'solid')
                    ws.cell(row = countRow, column = countColumn).font = Font(name = 'Arial', size = '11')
                    if i == 'id_tipo_doc':
                        valueRow = getattr(q.id_tipo_doc, 'tipo_doc', 'tipo_doc')
                    elif i == 'id_ficha':
                        numFicha = getattr(q.id_ficha, 'num_ficha', 'num_ficha')
                        nombreFicha = getattr(q.id_ficha, 'id_nombreficha', 'id_nombreficha')
                        valueRow = f'{numFicha}: {nombreFicha}'
                    elif i == 'id_rol':
                        valueRow = getattr(q.id_rol, 'tipo_rol', 'tipo_rol')
                    elif i == 'registro':
                        valueRow = str(getattr(q, i))
                    elif i == 'last_login':
                        valueRow = str(getattr(q, i)).split('+')[0]
                        if str(valueRow) == 'None':
                            valueRow = 'No ha ingresado al aplicativo'
                    else:
                        valueRow = getattr(q, i)
                    ws.cell(row=countRow, column=countColumn).value = valueRow
                    countRow += 1
                countColumn += 1

            # Nombre del archivo
            nombreArchivo = f'REPORTE {self.model.__name__.upper()}.xlsx'
            # Definir el tipo de respuesta
            response = HttpResponse(content_type = 'application/ms-excel')
            contenido = "attachment; filename = {0}".format(nombreArchivo)
            response['Content-Disposition'] = contenido
            wb.save(response)
            return response
        return render(request, self.template_name, {'usuarios': self.get_queryset()})

class crearUsuario(CreateView):
    model = Usuario
    template_name = 'usuarios/crear.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, request.FILES or None)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('usuarios')

class EditarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuarios/editar.html'
    form_class = UsuarioForm2
    if User.is_staff:
        success_url = reverse_lazy('usuarios')
    else:
        success_url = reverse_lazy('interfaz')

    def post(self, request, *args, **kwargs):
        if is_ajax(request=request):
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se pudo actualizar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            redirect('usuarios')


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