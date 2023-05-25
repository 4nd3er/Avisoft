from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # ! Modulo de inicio e interfaces
    path('', views.inicio, name="inicio"),
    path('inicio/', views.inicio, name="inicio"),
    path('registrarse/', views.registrarse, name="registrarse"),
    path('logout/', views.logout_usuario, name="logout"),
    path('contrasena/', views.contrasena, name="contrasena"),
    path('interfaz/', login_required(views.interfaz, login_url = 'inicio'), name="interfaz"),
    # path('interfaz_admin/', login_required(views.interfaz_admin, login_url = 'inicio'), name="interfaz_admin"),
    # ! Modulo de inicio e interfaces


    # ! Modulo de alimentacion
    path('alimentacion/', login_required(views.Alimentacionn.as_view(), login_url = 'inicio'), name="alimentacion"),
    path('crear_alimentacion/', login_required(views.crearAlimentacion.as_view(), login_url = 'inicio'), name="crear_alimentacion"),
    path('editar_alimentacion/<int:pk>', login_required(views.editarAlimentacion.as_view(), login_url = 'inicio'), name="editar_alimentacion"),
    path('confirmElimAlimentacion/<int:pk>', login_required(views.confirmarEliminarAlimentacion.as_view(), login_url = 'inicio'), name="confirmElimAlimentacion"),
    path('eliminarAlimentacion/<int:id>', login_required(views.eliminarAlimentacion), name="eliminarAlimentacion"),
    # ! Modulo de alimentacion


    # ! Modulo de detalle de jornada
    path('detalle_jornada/', login_required(views.DetalleJornadaa.as_view(), login_url = 'inicio'), name="detalle_jornada"),
    path('crear_detalle/', login_required(views.crearDetalle.as_view(), login_url = 'inicio'), name="crear_detalle"),
    path('editar_detalle/<int:pk>', login_required(views.editarDetalle.as_view(), login_url = 'inicio'), name="editar_detalle"),
    path('confirmElimDetalle/<int:pk>', login_required(views.confirmarEliminarDetalle.as_view(), login_url = 'inicio'), name="confirmElimDetalle"),
    path('eliminarDetalle/<int:id>', login_required(views.eliminarDetalle), name="eliminarDetalle"),
    # ! Modulo de detalle de jornada


    # ! Modulo de estados
    path('estados/', login_required(views.Estadoss.as_view(), login_url = 'inicio'), name="estados"),
    path('crear_estado/', login_required(views.crearEstado.as_view(), login_url = 'inicio'), name="crear_estado"),
    path('editar_estado/<int:pk>', login_required(views.editarEstado.as_view(), login_url = 'inicio'), name="editar_estado"),
    path('confirmElimEstado/<int:pk>', login_required(views.confirmarEliminarEstado.as_view(), login_url = 'inicio'), name="confirmElimEstado"),
    path('eliminarEstado/<int:estado>', login_required(views.eliminarEstado), name="eliminarEstado"),
    # ! Modulo de estados


    # ! Modulo de Fichas
    path('fichas/', login_required(views.Fichass.as_view(), login_url = 'inicio'), name="fichas"),
    path('crear_ficha/', login_required(views.crearFicha.as_view(), login_url = 'inicio'), name="crear_ficha"),
    path('editar_ficha/<int:pk>', login_required(views.editarFicha.as_view(), login_url = 'inicio'), name="editar_ficha"),
    path('confirmElimFicha/<int:pk>', login_required(views.confirmarEliminarFicha.as_view(), login_url = 'inicio'), name="confirmElimFicha"),
    path('eliminarFicha/<int:id_ficha>', login_required(views.eliminarFicha), name="eliminarFicha"),
    # ! Modulo de Fichas


    # ! Modulo de gallinas
    path('gallinas/', login_required(views.Gallinass.as_view(), login_url = 'inicio'), name="gallinas"),
    path('crear_gallinas/', login_required(views.crearGallinas.as_view(), login_url = 'inicio'), name="crear_gallinas"),
    path('editar_gallinas/<int:pk>', login_required(views.editarGallinas.as_view(), login_url = 'inicio'), name="editar_gallinas"),
    path('confirmElimGallinas/<int:pk>', login_required(views.confirmarEliminarGallinas.as_view(), login_url = 'inicio'), name="confirmElimGallinas"),
    path('eliminarGallinas/<int:id>', login_required(views.eliminarGallinas), name="eliminarGallinas"),
    # ! Modulo de gallinas


    # ! Modulo de galpones
    path('galpones/', login_required(views.Galponess.as_view(), login_url = 'inicio'), name="galpones"),
    path('crear_galpon/', login_required(views.crearGalpon.as_view(), login_url = 'inicio'), name="crear_galpon"),
    path('editar_galpon/<int:pk>', login_required(views.editarGalpon.as_view(), login_url = 'inicio'), name="editar_galpon"),
    path('confirmElimGalpon/<int:pk>', login_required(views.confirmarEliminarGalpon.as_view(), login_url = 'inicio'), name="confirmElimGalpon"),
    path('eliminarGalpon/<int:id>', login_required(views.eliminarGalpon), name="eliminarGalpon"),
    # ! Modulo de galpones
    

    # ! Modulo de jornadas
    path('jornadas/', login_required(views.Jornadass.as_view(), login_url = 'inicio'), name="jornadas"),
    path('crear_jornada/', login_required(views.crearJornada.as_view(), login_url = 'inicio'), name="crear_jornada"),
    path('editar_jornada/<int:pk>', login_required(views.editarJornada.as_view(), login_url = 'inicio'), name="editar_jornada"),
    path('confirmElimJornada/<int:pk>', login_required(views.confirmarEliminarJornada.as_view(), login_url = 'inicio'), name="confirmElimJornada"),
    path('eliminarJornada/<int:id>', login_required(views.eliminarJornada), name="eliminarJornada"),
    # ! Modulo de jornadas


    # ! Modulo de lineas
    path('lineas/', login_required(views.Lineass.as_view(), login_url = 'inicio'), name="lineas"),
    path('crear_linea/', login_required(views.crearLinea.as_view(), login_url = 'inicio'), name="crear_linea"),
    path('editar_linea/<int:pk>', login_required(views.editarLinea.as_view(), login_url = 'inicio'), name="editar_linea"),
    path('confirmElimLinea/<int:pk>', login_required(views.confirmarEliminarLinea.as_view(), login_url = 'inicio'), name="confirmElimLinea"),
    path('eliminarLinea/<int:id>', login_required(views.eliminarLinea), name="eliminarLinea"),
    # ! Modulo de lineas


    # ! Modulo de mortalidad y descarte
    path('mortalidad_descarte/', login_required(views.Mortalidadd.as_view(), login_url = 'inicio'), name="mortalidad_descarte"),
    path('crear_mortalidad/', login_required(views.crearMortalidad.as_view(), login_url = 'inicio'), name="crear_mortalidad"),
    path('editar_mortalidad/<int:pk>', login_required(views.editarMortalidad.as_view(), login_url = 'inicio'), name="editar_mortalidad"),
    path('confirmElimMortalidad/<int:pk>', login_required(views.confirmarEliminarMortalidad.as_view(), login_url = 'inicio'), name="confirmElimMortalidad"),
    path('eliminarMortalidad/<int:id>', login_required(views.eliminarMortalidad), name="eliminarMortalidad"),
    # ! Modulo de mortalidad y descarte


    # ! Modulo de produccion_diaria
    path('produccion_diaria/', login_required(views.ProduccionDiariaa.as_view(), login_url = 'inicio'), name="produccion_diaria"),
    path('crear_prod_diaria/', login_required(views.crearProdDiaria.as_view(), login_url = 'inicio'), name="crear_prod_diaria"),
    path('editar_prod_diaria/<int:pk>', login_required(views.editarProdDiaria.as_view(), login_url = 'inicio'), name="editar_prod_diaria"),
    path('confirmElimProdDiaria/<int:pk>', login_required(views.confirmarEliminarProdDiaria.as_view(), login_url = 'inicio'), name="confirmElimProdDiaria"),
    path('eliminarProdDiaria/<int:id>', login_required(views.eliminarProdDiaria), name="eliminarProdDiaria"),
    # ! Modulo de produccion_diaria


    # ! Modulo de rol
    path('rol/', login_required(views.Roll.as_view(), login_url = 'inicio'), name="rol"),
    path('crear_rol/', login_required(views.crearRol.as_view(), login_url = 'inicio'), name="crear_rol"),
    path('editar_rol/<int:pk>', login_required(views.editarRol.as_view(), login_url = 'inicio'), name="editar_rol"),
    path('confirmElimRol/<int:pk>', login_required(views.confirmarEliminarRol.as_view(), login_url = 'inicio'), name="confirmElimRol"),
    path('eliminarRol/<int:id>', login_required(views.eliminarRol), name="eliminarRol"),
    # ! Modulo de rol


    # ! Modulo de tipo de documento
    path('tipo_doc/', login_required(views.TipoDocc.as_view(), login_url = 'inicio'), name="tipo_doc"),
    path('crear_tipo_doc/', login_required(views.crearTipoDoc.as_view(), login_url = 'inicio'), name="crear_tipo_doc"),
    path('editar_tipo_doc/<int:pk>', login_required(views.editarTipoDoc.as_view(), login_url = 'inicio'), name="editar_tipo_doc"),
    path('confirmElimTipoDoc/<int:pk>', login_required(views.confirmarEliminarTipoDoc.as_view(), login_url = 'inicio'), name="confirmElimTipoDoc"),
    path('eliminarTipoDoc/<int:id>', login_required(views.eliminarTipoDoc), name="eliminarTipoDoc"),
    # ! Modulo de tipo de documento


    # ! Modulo de tipos de huevos
    path('tipos_huevos/', login_required(views.TiposHuevoss.as_view(), login_url = 'inicio'), name="tipos_huevos"),
    path('crear_tipo_huevo/', login_required(views.crearTipoHuevo.as_view(), login_url = 'inicio'), name="crear_tipo_huevo"),
    path('editar_tipo_huevo/<int:pk>', login_required(views.editarTipoHuevo.as_view(), login_url = 'inicio'), name="editar_tipo_huevo"),
    path('confirmElimTipoHuevo/<int:pk>', login_required(views.confirmarEliminarTipoHuevo.as_view(), login_url = 'inicio'), name="confirmElimTipoHuevo"),
    path('eliminarTipoHuevo/<int:id>', login_required(views.eliminarTipoHuevo), name="eliminarTipoHuevo"),
    # ! Modulo de tipos de huevos


    # ! Modulo de usuarios
    path('usuarios/', login_required(views.Usuarioss.as_view(), login_url = 'inicio'), name="usuarios"),
    path('crear_usuario/', login_required(views.crearUsuario.as_view(), login_url = 'inicio'), name="crear_usuario"),
    path('editar_usuario/<int:pk>', login_required(views.EditarUsuario.as_view(), login_url = 'inicio'), name="editar_usuario"),
    path('confirmElimUsuario/<int:pk>', login_required(views.confirmarEliminarUsuario.as_view(), login_url = 'inicio'), name="confirmElimUsuario"),
    path('eliminarUsuario/<int:id>', login_required(views.eliminarUsuario), name="eliminarUsuario"),
    # ! Modulo de usuarios
]