from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm



class GallinasForm(forms.ModelForm):
    class Meta:
        model = Gallinas
        fields = '__all__'
        labels = {
            'id_galpon': 'Galpon',
            'id_linea': 'Linea',
            'edad_sem': 'Edad en semanas',
            'peso_promedio':'Peso Promedio(Kg)',
        }

class LineaForm(forms.ModelForm):
    class Meta:
        model = Linea
        fields = '__all__'

class GalponesForm(forms.ModelForm):
    class Meta:
        model = Galpones
        fields ='__all__'
        labels = {
            'capac_bebed': 'Capacidad bebederos',
            'cant_bebed': 'Cantidad bebederos',
            'capac_comed': 'Capacidad comederos',
            'cant_comed': 'Cantidad comederos',
            'capac_gall': 'Capacidad gallinas',
            'cant_gall': 'Cantidad gallinas',
        }

class TiposHuevosForm(forms.ModelForm):
    class Meta:
        model = TiposHuevos
        fields ='__all__'

class EstadosForm(forms.ModelForm):
    class Meta:
        model = Estados
        fields = ['descrip']

class TipoDocForm(forms.ModelForm):
    class Meta:
        model = TipoDoc
        fields = ['tipo_doc']
        widgets = {
            'tipo_doc': forms.TextInput(attrs = {'class': 'form-control'}),
        }

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = '__all__'

class AlimentacionForm(forms.ModelForm):
    class Meta:
        model = Alimentacion
        fields = '__all__'
        labels = {
            'id_galpon': 'Galpon',
            'gr_gallina_dia': 'Gr/Gallina/Dia',
        }

class DetalleJornadaForm(forms.ModelForm):
    class Meta:
        model = DetalleJornada
        fields = '__all__'
        labels = {
            'id_galpon': 'Galpon',
            'id_jornada': 'Jornada',
        }

class JornadaForm(forms.ModelForm):
    class Meta:
        model = Jornada
        fields = '__all__'

class MortalidadDescarteForm(forms.ModelForm):
    class Meta:
        model = MortalidadDescarte
        fields = '__all__'
        labels = {
            'id_galpon': 'Galpon',
            'cant_muertas': 'Cantidad muertas',
            'cant_descarte': 'Cantidad de descarte',
            'id_tipo_descarte': 'Tipo de Descarte'
        }

class ProduccionDiariaForm(forms.ModelForm):
    class Meta:
        model = ProduccionDiaria
        fields = '__all__'
        #para que no se muestre en el formulario y se establezca automatica en la vista
        exclude = ['id_usuario']  # Excluir el campo id_usuario del formulario
        labels = {
            'id_detalle_jornada': 'Detalle de Jornada',
            'id_tipo_huevo': 'Tipo de huevo',
            'cantidad': 'Cantidad',
            'fecha': 'fecha',
            'id_usuario': 'Usuario',
        }

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'
        labels = {'tipo_rol' : 'Rol'}

class UsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellido': forms.TextInput(attrs = {'class': 'form-control'}),
            'correo': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs = {'class': 'form-control'}),
            'direccion': forms.TextInput(attrs = {'class': 'form-control'}),
            'id_tipo_doc': forms.Select(attrs = {'class': 'form-control'}),
            'id_ficha': forms.Select(attrs = {'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }
    id_tipo_doc = forms.ModelChoiceField(queryset = TipoDoc.objects.all(), label = 'Tipo de documento')
    id_ficha = forms.ModelChoiceField(queryset = Ficha.objects.all(), label = 'Ficha')
    id_rol = forms.ModelChoiceField(queryset = Rol.objects.all(), label = 'Rol')
    password2 = forms.CharField(label = 'Contraseña de confirmacion', widget = forms.PasswordInput())\

class UsuarioForm2(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellido': forms.TextInput(attrs = {'class': 'form-control'}),
            'correo': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs = {'class': 'form-control'}),
            'direccion': forms.TextInput(attrs = {'class': 'form-control'}),
            'id_tipo_doc': forms.Select(attrs = {'class': 'form-control'}),
            'id_ficha': forms.Select(attrs = {'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }
    id_tipo_doc = forms.ModelChoiceField(queryset = TipoDoc.objects.all(), label = 'Tipo de documento')
    id_ficha = forms.ModelChoiceField(queryset = Ficha.objects.all(), label = 'Ficha')
    id_rol = forms.ModelChoiceField(queryset = Rol.objects.all(), label = 'Rol')

class contrasenaForm(forms.ModelForm):
    template_name = 'registration/password_reset_form.html'
    fields = '__all__'
    email = forms.EmailField(label = 'Correo electronicoooo', widget = forms.EmailInput(attrs = {'class': 'form-control'}))