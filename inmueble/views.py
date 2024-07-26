from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from main.models import Inmueble , Region, Comuna , UserProfile
from main.services import crear_inmueble as crear_inmueble_service, editar_inmueble as editar_inmueble_service, eliminar_inmueble as eliminar_inmueble_service
#from inmueble.forms import InmuebleForm
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

def solo_propietarios(user):
    id_usuario = requers.user.id
    propiedades = Inmueble.objects.filter(propietario_id = id_usuario)
    

@login_required
@user_passes_test(solo_arrendadores)
def editar_inmueble(req, id):
    if req.method == 'GET':
        # 1 obtengo el inmueble
        inmueble= Inmueble.objects.get(id=id)
        # 2 obtengo la regiones y comunas
        regiones = Region.objects.all()
        comunas = Comuna.objects.all()
        #2.5 obtengo el codigo de la region
        cod_region = inmueble.comuna.region.cod
        context={
            'inmueble':inmueble,
            'regiones': regiones,
            'comunas':comunas,
            'cod_region': cod_region
            
        }
        print ('editando el inmueble'+id)
        
        return render(req, 'editar_inmueble.html', context)
    else:
        #req.method == 'POST'
        propietario_rut = req.user.username
        editar_inmueble_service(
            id,
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
        messages.success(req, 'propiedad editada exitosamente')
        return redirect ('/accounts/profile/')
        

@user_passes_test(solo_arrendadores)
def eliminar_inmueble(req, id):
    eliminar_inmueble_service(id)
    messages.error(req,'Inmueble ha sido eliminado')
    return redirect ('/accounts/profile/')


@login_required
def detalle_inmueble(req, id):
    id=int(id)
    inmueble_encontrado = Inmueble.objects.get(id=id)
    
    context ={
        'inmueble':inmueble_encontrado
    }
    return render(req, 'detalle_inmueble.html', context)