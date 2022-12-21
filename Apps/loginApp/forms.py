from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.core import validators

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','rut','telefono','password1','password2']
        help_text = {k:"" for k in fields } 



class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario'}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario'})
        }



# class AutenticarseForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fiels = ['username', 'password']










# class FormularioRegistroUsuario(forms.ModelForm):
#     password1 = forms.CharField(label= 'Contraseña 1', widget = forms.PasswordInput(attrs ={
#         'class':'form-control',
#         'placeholder': 'Ingrese su contraseña....'
#     }))
#     password2 = forms.CharField(label= 'Contraseña 2', widget = forms.PasswordInput(attrs = {
#         'class':'form-control',
#         'placeholder': 'Ingrese de nuevo su contraseña....'
#     }))

#     class Meta:
#         model = Usuario
#         fields = ('email','rut','username','nombre')
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Correo electronico'}),
#             'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Rut'}),
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre de Usuario'}),
#             'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}),
#         }
#     def clean_password2(self):

#         print(self.cleaned_data)
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 != password2:
#             raise forms.ValidationError('Contraseña no coinciden')
#         return password2

#     def save(self, commit = True):
#         user = super().save(commit = False)
#         user.set_password(self.cleaned_data['password1'])
#         if commit:
#             user.save()
#         return user
