from django import forms
from Apps.loginApp.models import *

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['numeroEstacionamiento','estado']
        # Gracias a los widgets le podemos pasar a los formularios diferentes clases o atributos
        widgets = {
            'numeroEstacionamiento': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'N° de estacionamiento'}),
            'estado' : forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class VetarUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['estado']
        # Gracias a los widgets le podemos pasar a los formularios diferentes clases o atributos
        widgets = {
            'estado' : forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
            
# class ReservaForm(forms.ModelForm):
#     class Meta:
#         model = Reserva
#         fields = ['fecha','horaInicio','horaTermino','numeroEstacionamiento']
#         # Gracias a los widgets le podemos pasar a los formularios diferentes clases o atributos
#         widgets = {
            
#             'fecha' : forms.TextInput(attrs={'type':'date'}),
#             'horaInicio' : forms.TextInput(attrs={'type':'time'}),
#             'horaTermino' : forms.TextInput(attrs={'type':'time'}),
#         #     'horaTermino' : forms.DurationField(attrs={'class':'form-control mt-3', 'placeholder':'Ingrese la hora de termino de su reserva'}),
#         #     'numeroEstacionamiento': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'N° de estacionamiento'}),
#         }
            