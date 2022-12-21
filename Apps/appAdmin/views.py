from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Apps.loginApp.models import User, Reserva
from Apps.sReservas.models import Lugar
from .forms import *
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponse
from .utils import render_to_pdf
from Apps.sReservas.forms import *
from django.contrib import messages
from Apps.loginApp.forms import *
# pip freeze > requirements. txt  --------> Funciona para desplegar mas facil

# LIBRERIAS

# pip install xhtml2pdf ----> para los reportes

# Create your views here.

# nombre y contraseña superuser MatiasZ 21204650

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def funcionesAdmin(request):
    return render(request, 'panelAdmin.html')

@login_required
def adminEstacionamiento(request):
    return render(request, 'adminEstacinamiento.html')

@login_required
def generarReportes(request):
    return render(request, 'generarReportes.html')

@login_required
def verUsers(request, user_id):
    users = User.objects.get(id=user_id)
    return render(request, 'mostrarUsers.html',{'usuario':users})

#-----------------------------------------------------------------------
@login_required
def vetarUsuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    if usuario.estado == True:
        usuario.estado = False
        usuario.save()
        messages.success(request,'Se a vetado el usuario')
    # return render(request, 'buscarUsuariosAdmin.html',{'alert':f'se a betado al usuario : {self} '})
    return redirect('buscador')

#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
@login_required
def anularVetarUsuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    if usuario.estado == False:
        usuario.estado = True
        usuario.save()
    # return render(request, 'buscarUsuariosAdmin.html',{'alert':f'se a betado al usuario : {self} '})
    return redirect('buscador')
#-----------------------------------------------------------------------


@login_required
def buscarUsuariosAdmin(request):
    busqueda = request.GET.get('buscado')
    usuariosList = User.objects.all()
    if busqueda:
        usuariosList = User.objects.filter(username__icontains = busqueda) 
     
    return render(request, 'buscarUsuariosAdmin.html',{'usuarios':usuariosList})

@login_required
def crearEstacionamiento(request):
    if request.method == 'POST':
        formEstacionamiento = EstacionamientoForm(request.POST)
        if formEstacionamiento.is_valid():
                formEstacionamiento.save()
                return redirect('InicioAdmin')
    return render(request, 'crearEstacionamiento.html',{'formEstacionamiento': EstacionamientoForm})
    

@login_required
def listarEstacionamientoDisponible(request):
    estacionamiento = Estacionamiento.objects.filter(estado = False)
    return render(request, 'listarEstacionamiento.html',{'estacionamientos':estacionamiento, 'title':'Estacionamientos disponibles'})

@login_required
def listarEstacionamientoNoDisponible(request):
    estacionamiento = Estacionamiento.objects.filter(estado = True)
    return render(request, 'listarEstacionamiento.html',{'estacionamientos':estacionamiento, 'title':'Estacionamientos No disponibles'})

@login_required
def generar_reporte_reservas(request):
    # Obtengo los datos de la base de datos
    lugar = Lugar.objects.all()
    user = User.objects.all()
    estacionamiento = Estacionamiento.objects.all()
    data = {
        'count': lugar.count(),
        'lugar': lugar,
        'contaruser': user.count(),
        'user': user,
        'contarestacionamineto': estacionamiento.count(),
        'estacionamiento': estacionamiento,
    }
    return render_to_pdf('reportes.html', data) # Voy a buscar mi funcion desde el utils y le paso mi html y mis datos

@login_required
def selecionarReporte(request):
    busqueda = request.GET.get('desde')
    reservas = Lugar.objects.all()
    if busqueda:
        reservas = Lugar.objects.filter(fecha = busqueda) 

    return render(request, 'seleccionarReporte.html', {'reservas':reservas})
