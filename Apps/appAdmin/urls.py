from django.urls import path, include
from . import views 
from .views import generar_reporte_reservas

urlpatterns = [
    path('logout/', views.signout, name='logout'),
    path('inicio-admin/', views.funcionesAdmin, name='InicioAdmin'),
    path('administrar-estacionamiento/', views.adminEstacionamiento, name='adEstacionamiento'),
    path('agregar-estacionamiento/', views.crearEstacionamiento, name='crearEstacionamiento'),
    path('listar-estacionamientos-disponibles/', views.listarEstacionamientoDisponible, name='EstDisponible'),
    path('listar-estacionamientos-NO-disponibles/', views.listarEstacionamientoNoDisponible, name='EstNoDisponible'),
    path('buscador-usuarios/', views.buscarUsuariosAdmin, name='buscador'),
    path('seleccionar-reporte/', views.selecionarReporte, name='seleccionarReportes'),
    # path('generar-reserva/', views.generarReserva, name='generarReservaUsuario'),
    # path('generar-reserva-usuario/<int:estacionamiento_id>', views.reservaUsuario, name='reservaUsuario'),
    path('reporte-reserva/', generar_reporte_reservas, name='reportesReservas'),
    path('vetar-user/<int:user_id>',views.vetarUsuario, name='vetarUser'),
    path('anular-vetar-user/<int:user_id>',views.anularVetarUsuario, name='anularVetarUser'),
    path('ver-user/<int:user_id>',views.verUsers, name='verUsers'),
]