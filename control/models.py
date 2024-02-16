# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key = True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Alimentacion(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.DateField(auto_now_add = True)
    id_galpon = models.ForeignKey('Galpones', on_delete = models.CASCADE, db_column = 'id_galpon')
    gr_gallina_dia = models.CharField(db_column = 'Gr/Gallina/Dia', max_length=10)
    kg_total = models.CharField(max_length=10)
    bultos_total = models.CharField(max_length=10)
    c_a = models.CharField(max_length=10)
    id_tipo_alimento = models.ForeignKey('TipoAlimento', models.DO_NOTHING, db_column='id_tipo_alimento')

    def __str__(self):
        return f'{self.kg_total} Kg'

    class Meta:
        managed = False
        db_table = 'alimentacion'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    documento = models.IntegerField()
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    fecha_regis = models.DateField(auto_now_add = True)
    num_ficha = models.CharField(max_length=50)
    id_nombreficha = models.ForeignKey('Nombreficha', models.DO_NOTHING, db_column='id_nombreFicha')  # Field name made lowercase.
    estado_ficha = models.IntegerField()

    def __str__(self):
        return f'{self.num_ficha}: {self.id_nombreficha.nombre}'

    class Meta:
        managed = False
        db_table = 'ficha'


class Gallinas(models.Model):
    id = models.AutoField(primary_key = True)
    id_galpon = models.ForeignKey('Galpones', on_delete = models.CASCADE, db_column = 'id_galpon')
    id_linea = models.ForeignKey('Linea', on_delete = models.CASCADE, db_column = 'id_linea')
    fecha_ingreso = models.DateField(auto_now_add = True)
    cantidad_gallinas = models.PositiveIntegerField()
    peso_promedio = models.PositiveIntegerField()
    edad_sem = models.PositiveIntegerField()
    procedencia = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.cantidad_gallinas} gallinas'
    
    class Meta:
        managed = False
        db_table = 'gallinas'
        verbose_name="Gallina"
        verbose_name_plural="Gallinas"
    


class Galpones(models.Model):
    fecha = models.DateField(auto_now_add = True)
    nombre_galpon = models.CharField(max_length = 100, unique=True)
    ancho = models.IntegerField(
        validators=[
            MinValueValidator(1, message='El número debe ser mayor o igual a 0.'),
            MaxValueValidator(900, message='El número debe ser menor o igual a 900.'),
            RegexValidator(r'^\d+$', 'Ingrese un número entero válido sin comas, puntos ni signos.')
        ]
    )
    largo = models.IntegerField(
        validators=[
            MinValueValidator(1, message='El número debe ser mayor o igual a 0.'),
            MaxValueValidator(900, message='El número debe ser menor o igual a 900.'),
            RegexValidator(r'^\d+$', 'Ingrese un número entero válido sin comas, puntos ni signos.')
        ]
    )
    area = models.IntegerField()
    capac_bebed = models.IntegerField()
    cant_bebed = models.IntegerField(
        validators=[
            MinValueValidator(1, message='El número debe ser mayor o igual a 0.'),
            MaxValueValidator(900, message='El número debe ser menor o igual a 900.'),
            RegexValidator(r'^\d+$', 'Ingrese un número entero válido sin comas, puntos ni signos.')
        ]
    )
    capac_comed = models.IntegerField()
    cant_comed = models.IntegerField(
        validators=[
            MinValueValidator(1, message='El número debe ser mayor o igual a 0.'),
            MaxValueValidator(900, message='El número debe ser menor o igual a 900.'),
            RegexValidator(r'^\d+$', 'Ingrese un número entero válido sin comas, puntos ni signos.')
        ]
    )
    capac_gall = models.IntegerField()
    cant_gall = models.IntegerField(
        validators=[
            MinValueValidator(1, message='El número debe ser mayor o igual a 0.'),
            MaxValueValidator(900, message='El número debe ser menor o igual a 900.'),
            RegexValidator(r'^\d+$', 'Ingrese un número entero válido sin comas, puntos ni signos.')
        ]
    )
    capac_nidales = models.IntegerField()
    cant_nidales = models.IntegerField(
        validators=[
            MinValueValidator(1, message='El número debe ser mayor o igual a 0.'),
            MaxValueValidator(900, message='El número debe ser menor o igual a 900.'),
            RegexValidator(r'^\d+$', 'Ingrese un número entero válido sin comas, puntos ni signos.')
        ]
    )

    def __str__(self):
        return f'{self.nombre_galpon}'

    class Meta:
        managed = False
        db_table = 'galpones'
        ordering = [('-id')]


class Jornada(models.Model):
    jornada = models.CharField(max_length = 50)

    def __str__(self):
        return self.jornada

    class Meta:
        ordering = [('id')]
        managed = False
        db_table = 'jornada'


class Linea(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'linea'


class MortalidadDescarte(models.Model):
    fecha = models.DateField()
    id_galpon = models.ForeignKey(Galpones, models.DO_NOTHING, db_column='id_galpon')
    cant_muertas = models.IntegerField()
    cant_descarte = models.IntegerField()
    id_tipo_descarte = models.ForeignKey('TipoDescarte', models.DO_NOTHING, db_column='id_tipo_descarte')
    saldo = models.PositiveIntegerField()

    def __str__(self):
        return  f"{self.id_tipo_descarte} {str(self.fecha)}"
    
    class Meta:
        managed = False
        db_table = 'mortalidad_descarte'


class Nombreficha(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'nombreficha'


class ProduccionDiaria(models.Model):
    id_galpon = models.ForeignKey(Galpones, models.DO_NOTHING, db_column='id_galpon')
    id_jornada = models.ForeignKey(Jornada, models.DO_NOTHING, db_column='id_jornada')
    id_tipo_huevo = models.ForeignKey('TiposHuevos', models.DO_NOTHING, db_column='id_tipo_huevo')
    cantidad = models.IntegerField()
    rotos = models.IntegerField()
    descarte = models.IntegerField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    fecha = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'jornada {self.id_jornada}, Tipo de huevo: {self.id_tipo_huevo}, cantidad: {self.cantidad}'

    class Meta:
        managed = False
        db_table = 'produccion_diaria'


class Registrodiario(models.Model):
    id_galpon = models.ForeignKey(Galpones, models.DO_NOTHING, db_column='id_galpon')
    id_gallinas = models.ForeignKey(Gallinas, models.DO_NOTHING, db_column='id_gallinas')
    id_alimentacion = models.ForeignKey(Alimentacion, models.DO_NOTHING, db_column='id_alimentacion')
    id_producciondiaria = models.ForeignKey(ProduccionDiaria, models.DO_NOTHING, db_column='id_produccionDiaria')
    id_mortades = models.ForeignKey(MortalidadDescarte, models.DO_NOTHING, db_column='id_mortaDes')
    fecha = models.DateField(auto_now_add = True)

    class Meta:
        managed = False
        db_table = 'registrodiario'


class Rol(models.Model):
    tipo_rol = models.CharField(max_length = 30)

    def __str__(self):
        return self.tipo_rol

    class Meta:
        managed = False
        db_table = 'rol'


class TipoAlimento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'tipo_alimento'


class TipoDescarte(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = 'tipo_descarte'


class TipoDoc(models.Model):
    id = models.IntegerField(primary_key = True)
    tipo_doc = models.CharField(max_length = 30)

    def __str__(self):
        return self.tipo_doc

    class Meta:
        managed = False
        db_table = 'tipo_doc'


class TiposHuevos(models.Model):
    tipos_huevos = models.CharField(max_length = 10)

    def __str__(self):
        return self.tipos_huevos

    class Meta:
        managed = False
        db_table = 'tipos_huevos'


class UsuarioManager(BaseUserManager):
    def create_user(self, documento, nombre, apellido, password = None):

        usuario = self.model(
            documento = documento,
            nombre = nombre,
            apellido = apellido
        )

        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, documento, nombre, apellido, password):
        usuario = self.create_user(
            documento = documento,
            nombre = nombre,
            apellido = apellido,
            password = password
        )

        usuario.is_staff = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    id_tipo_doc = models.ForeignKey(TipoDoc, on_delete = models.CASCADE, db_column = 'id_tipo_doc', null = True, blank = True)
    documento = models.IntegerField('Numero de documento', unique = True,
    validators = [
        MinValueValidator(3400000, "Digite un numero de documento valido")
    ])
    celular = models.IntegerField(
    validators = [
        MinValueValidator(3000000000, "Digite un numero de telefono valido")
    ])
    email = models.EmailField(max_length = 100, db_column = 'correo', unique = True)
    id_ficha = models.ForeignKey(Ficha, on_delete = models.CASCADE, db_column = 'id_ficha', null = True, blank = True)
    id_rol = models.ForeignKey(Rol, on_delete = models.CASCADE, db_column = 'id_rol', null = True, blank = True)
    password = models.CharField(max_length = 255, null = True, blank = True)
    imagen = models.ImageField(upload_to = 'imagen_usuario', db_column = 'imagen', null = True, blank = True)
    registro = models.DateField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now = True, null = True, blank = True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_satff(self):
        return self.is_staff

    class Meta:
        ordering = [('-id')]
        managed = False
        db_table = 'usuario'


class Vacunas(models.Model):
    idvacunas = models.AutoField(db_column='Idvacunas', primary_key=True)  # Field name made lowercase.
    nombrev = models.CharField(db_column='Nombrev', max_length=60)  # Field name made lowercase.
    presentacion = models.CharField(db_column='Presentacion', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vacunas'