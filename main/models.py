
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='usuario', on_delete = models.CASCADE)
    direccion = models.CharField(max_length= 255)
    telefono = models.CharField(max_length=255 , null=True)



class Comuna(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    
    def _str__(self):
        return self.nombre



    
class Inmueble(models.Model):
    inmueble_tipo=(
        ('casa','Casa'),
        ('depto','Departamento'),
        ('par','Parcela')
    )
    nombre = models.CharField(max_length=50)
    descripcion=models.TextField(max_length=1500)
    M2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    M2_totales_terreno = models.IntegerField(validators=[MinValueValidator(1)])
    cant_estacionamientos = models.IntegerField(validators=[MinValueValidator(1)])
    cant_habitaciones= models.IntegerField(validators=[MinValueValidator(1)], default=1)
    cant_banos=models.IntegerField(validators=[MinValueValidator(0)], default=0)
    direccion= models.CharField(max_length=255)
    tipo_vivienda= models.CharField(max_length=100, choices=inmueble_tipo, default='desconocido')
    precio_mensual= models.IntegerField(validators=[MinValueValidator(1000)])
    # precio= models.IntegerField(validators=[MinValueValidator(1000)], null=True)
    # precio_ufs= models.FloatField(validators=[MinValueValidator(1.0)], null=True)
    
    comuna = models.ForeignKey(Comuna,related_name='inmuebles', on_delete = models.RESTRICT)
    propietario= models.ForeignKey (User, on_delete=models.RESTRICT, related_name='inmuebles')
# class region : PDTE

    
    
class Solicitud(models.Model):
    estados =(('pendiente','Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'aprobada'))
    
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
    arrendador =models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes')
    fecha =models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length = 50, choices=estados)
    
