from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.loginFuncion, name='login'),
]