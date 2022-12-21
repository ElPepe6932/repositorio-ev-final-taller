from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from Apps.loginApp.models import *
from .forms import AgregarVehiculo , Reser , Lugar
from django.contrib.auth import authenticate,login
# from .forms import EstacionamientosForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from Apps.appAdmin.forms import EstacionamientoForm
# Create your views here.



# htmls



def home(request):
    
    return render(request, 'InicioUsuario.html')



def boleta(request,id_lugar):

    
    termino = Lugar.objects.get(id=id_lugar)

    if termino.activo == True:
        termino.termino = timezone.now()
        termino.save()
    else:
        termino.save()

    #total_pagar= (termino.total == ('termino.inicio') - ('termino.termino'))


    return render(request, 'boleta.html', {'termino':termino, })

def boletatermino(request,numero_id,lugar_id):

    activo = Lugar.objects.get(id=lugar_id)
    termino = Estacionamiento.objects.get(id=numero_id)

    if activo.activo == True:
        activo.activo = False
        termino.estado = False
        termino.save()
        activo.save()
    else:
        termino.save()
        activo.save()

    return redirect( 'InicioUser')




def soporte(request):
    historial = Lugar.objects.filter(user=request.user)
    return render(request, 'soporte.html', {'historial':historial})




def info(request):
    return render(request, 'info.html')

    

def lista(request):
    automovil = Vehiculo.objects.filter(owner=request.user) 
    
    data = {'automovil':automovil}

    return render(request, 'lista.html', data)
    






def base(request):

    return render(request, 'base.html')    


#--------------------------------------------------------------------------------------------------------------

#Agregar vehiculo




def agregar(request):


    if request.method == 'POST':
        formulario = AgregarVehiculo(request.POST)
        if formulario.is_valid():
            new_car = formulario.save(commit=False)
            new_car.owner = request.user
            new_car.save()
            messages.success(request, 'Agregado Correctamente')
            return redirect('lista')
            
        else:
            formulario = AgregarVehiculo
    else:
        return render(request, 'agregar.html', {'form':AgregarVehiculo})






#-------------------------------------------------------------------------------------------------------------------
#EstacionamientosReservas

def listaReserva(request):
   
    estacionamiento = Estacionamiento.objects.filter()
    
    return render(request, 'generarReserva.html', {'estacionamientos': estacionamiento  })



def reservaPrueba(request, estacionamiento_id):
    task = get_object_or_404(Estacionamiento, pk = estacionamiento_id)  
    form = EstacionamientoForm
    
    if request.method == 'POST':
        task = get_object_or_404(Estacionamiento, pk = estacionamiento_id)    
        form = EstacionamientoForm(request.POST, instance=task)
        return redirect('generarReserva')
    return render(request, 'reserva/mostrar.html',{'form': form, 'task':task})

    



def datosres(request, numero_id):
    
    numero = Estacionamiento.objects.get(id=numero_id)
    
    if request.method == 'POST':
        formulario = Reser(request.POST)
        if formulario.is_valid():
            new_car = formulario.save(commit=False)
            new_car.user = request.user
            new_car.numero_id = numero_id
            numero.estado = True
            numero.save()
            new_car.save()
            
            messages.success(request, 'Reservado correctamente')    
        return redirect('soporte')       
    else:

        return render(request, 'reserva/mostrar.html', {'form':Reser})