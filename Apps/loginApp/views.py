from django.shortcuts import render, redirect
# from .forms import FormularioRegistroUsuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistroForm , LoginForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'info.html',{'title':'Bienvenido'})

def registro(request):
   formR = RegistroForm()
   if request.method == 'POST':
        formR = RegistroForm(request.POST)
        if formR.is_valid():
            formR.save()
            return redirect('InicioUser')
            
    
   return render(request, 'registro.html',{'formR': formR})

def loginFuncion(request):
    formA = AuthenticationForm()
    if request.method == 'POST': 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request,'login.html',{'formA' : formA, 'error':'Nombre de usuario o contraseña incorrecta¡¡'})
        
        else:

            if user.estado == False:
                
                # messages.error(request ,'Error tu cuenta se encuentra suspendida')
                return render(request, 'login.html', {'mensaje':'Error tu cuenta se encuentra suspendida'} )
            
            else:
                 if user.is_staff:
                    login(request, user) 
                    return redirect('InicioAdmin')
            
                 else:
                    login(request, user)
                    return redirect('InicioUser')


           
           # Hacer if para que devuelva a django admin o django user
            

    else:
        return render(request,'login.html',{'formA': formA})

