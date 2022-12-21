from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    rut = models.CharField(max_length=10, null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    estado = models.BooleanField(default=True ,null=True)
    def __str__(self):
        return f'Nombre de usuario: {self.username} ________ RUT del usuario: {self.rut}'

class Vehiculo(models.Model):
    patente = models.CharField(max_length=8)
    modeloVehiculo = models.CharField(max_length=40)
    colorVehiculo = models.CharField(max_length=40)
    yearVehiculo = models.DateField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Vehiculo: {self.modeloVehiculo} | Con patente: {self.patente}' 



class Estacionamiento(models.Model):
    numeroEstacionamiento = models.IntegerField(unique=True)   
    estado = models.BooleanField(default=False, null=True)
    def __str__(self):
        return f'N° Estacionamiento: {self.numeroEstacionamiento} | Estado del estacionamiento: {self.estado}' 
    # (como mostrar los estacionamientos disponibles y los no disponibles 
    # estacionamineto = Estacionamiento.objects.filter(user=request.user, estado = True).order_by('-datecompleted'))



class Reserva(models.Model):
    # fecha = models.CharField(max_length=20)
    horaInicio = models.CharField(max_length=20,default=7)
    # horaTermino = models.CharField(max_length=20)
    owner = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    numeroEstacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    def __str__(self):
        return f'Nombre de usuario: {self.owner.owner.username}, numero estacionamiento: {self.numeroEstacionamiento.numeroEstacionamiento} '










# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# # Create your models here.



# class UsuarioManager(BaseUserManager):
#     def create_user(self,email,username,rut,nombre,password = None):
#         if not email:
#             raise ValueError('El usuario debe tener email')

#         usuario = self.model(
#             username = username,
#             email = self.normalize_email(email), 
#             rut = rut,
#             nombre = nombre
#         )

#         usuario.set_password(password)
#         usuario.save()
#         return usuario

#     def create_superuser(self, email, username, rut, nombre, password):
#         usuario = self.create_user(
#             email,
#             username=username,
#             rut=rut,
#             nombre=nombre,
#             password=password
#         )
#         usuario.usuario_tipo = True
#         usuario.save()
#         return usuario




# class Usuario(AbstractBaseUser):
#     username = models.CharField('Nombre de Usuario',unique=True, max_length=100)
#     rut = models.CharField('RUT ',unique=True, max_length=10)
#     email = models.EmailField('Correo electronico ',unique=True, max_length=254)
#     nombre = models.CharField('Nombre ',max_length=200, null=True)
#     usuario_activo = models.BooleanField(default=True)
#     usuario_tipo = models.BooleanField(default=False)
#     objects = UsuarioManager() 

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['rut','email','nombre']

#     def __str__(self):
#         return f'Usuario {self.username}'

#     def has_perm(self, perm, obj = None):
#         return True

#     def has_module_perms(self,app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.usuario_tipo

