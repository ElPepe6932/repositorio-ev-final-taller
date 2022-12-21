from django.db import models
from Apps.loginApp.models import *
from django.utils import timezone
# from Apps.loginApp.models import User

# # Create your models here.



# class Vehiculo(models.Model):
#     patente = models.CharField(max_length=50)
#     modelo = models.CharField(max_length=50)
#     color = models.CharField(max_length=50)
#     año = models.CharField(max_length=50)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.patente + '- de ' + self.user.username

# class Reserva(models.Model):
#     estacionamiento = models.CharField(max_length=50)
#     estado = models.BooleanField(default = True, verbose_name='Disponibilidad' )

#     def __str__(self):
#         return self.estacionamiento 


class Lugar(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     numero = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
     vehiculo= models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
     inicio = models.DateTimeField(default=timezone.now)
     termino =models.DateTimeField(null=True, blank=True)
     activo = models.BooleanField(default=True, null=True)
     total =models.CharField(max_length=50,null=True, blank=True)
     def __str__(self):
          return f'Hora inicio: {self.inicio} Hora termino {self.termino}' 
     

    