from django import forms
from . models import *
from Apps.loginApp.models import * 
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User  

# class CustomUserCreationForm(UserCreationForm):
    

    
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

#         help_text = {k:"" for k in fields }


class AgregarVehiculo(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ['patente', 'modeloVehiculo', 'colorVehiculo', 'yearVehiculo']
       

        widgets= {

          'yearVehiculo': forms.TextInput(attrs={'type':'date', 'class':'form-control'})
        }    

# class LoginUsuario(UserCreationForm):

#     class Meta:
#         model = Usuario
#         fields = ['username', 'correo', 'rut', 'telefono', 'contraseña']



# Reservas

# class ListadoReserva ():
#     class Meta:
#         model = Reserva
#         fields = ['estacionamiento', 'estado' ]

class Reser(forms.ModelForm):
     class Meta:
         model = Lugar
         fields = ['vehiculo' ]

 #        widgets= {

#          'inicio': forms.TextInput(attrs={'type':'time',  'class':'form-control'}),
#           'horaInicio': forms.TextInput(attrs={'type':'time', 'class':'form-control'}),
#           'horaTermino': forms.TextInput(attrs={'type':'time',  'class':'form-control'}),

#        }    
           