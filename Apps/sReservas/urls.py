from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
     path('listaUser/', views.lista, name='lista'),
     path('agregarUser/', views.agregar, name='agregar'),
     path('listaReserva/', views.listaReserva, name='generarReserva'),
     # path('formres/<int:estacionamiento_id>', views.datosres, name='formres'),
     path('homeUser/', views.home, name='InicioUser'),
     path('soporteUser/', views.soporte, name='soporte'),
     path('infoUser/', views.info, name='info'),
     path('prueba-reserva/<int:numero_id>', views.datosres, name='reservaPrueba'),
     # path('reservar-estacionamiento/', RegistrarReserva.as_view, name='reservarEstacionamiento'),
     path('boleta/<int:id_lugar>', views.boleta, name='boleta'),
     path('boleta-termino/<int:numero_id>/<int:lugar_id>', views.boletatermino, name='termino'),
     #path('termino-reser/', views.terminar, name='date'),
     

    
]
