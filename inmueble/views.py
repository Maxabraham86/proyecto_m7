from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from main.models import Inmueble, Region, Comuna
from django.http import HttpResponse 
from main.services import crear_inmueble as crear_inmueble_service
from django.contrib.auth.decorators import login_required

# Create your views here.

def solo_arrendadores(user):
    if user.usuario.rol == 'arrendador' or user.is_staff == True:
        return True
    else:
        messages.error(req,' Sal de aca')
        return False


@login_required
@user_passes_test(solo_arrendadores)
def nuevo_inmueble(req):
    # pasar los datos requeridos por el formulario
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    context={
        'tipos_inmueble': Inmueble.inmueble_tipo,
        'regiones': regiones,
        'comunas': comunas
    }
    
    return render(req,'nuevo_inmueble.html', context)


@user_passes_test(solo_arrendadores)
def crear_inmueble(req):
        #imprimimos lo que llega al formulario
    propietario_rut = req.user.username
    crear_inmueble_service(
        req.POST['nombre'],
        req.POST['descripcion'],
        int(req.POST['M2_construidos']),
        int(req.POST['M2_totales_terreno']),
        int(req.POST['cant_estacionamientos']),
        int(req.POST['cant_habitaciones']),
        int(req.POST['cant_banos']),
        req.POST['direccion'],
        int(req.POST['precio_mensual']),
        req.POST['tipo_vivienda'],
        req.POST['comuna_cod'],
        propietario_rut
        )
    
    messages.success(req, 'propiedad agregada exitosamente')
    return redirect ('/accounts/profile/')
