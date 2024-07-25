from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django import template
from main.services import editar_user_sin_password, cambio_pass, crear_inmueble, crear_user
from main.models import Inmueble, Comuna, Region

#from django.contrib.auth import user

def success(req):
    return render(req,'exito.html')

def form_test(req):
    return render (req,'form_test.html')

@login_required
def index(req):
    datos = req.GET
    region_cod = datos.get('region_cod', '')
    comuna_cod = datos.get('comuna_cod', '')
    palabra = datos.get('palabra', '')
    
    inmuebles = filtrar_inmuebles(region_cod, comuna_cod, palabra)
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    context = {
        'comunas':comunas,
        'regiones': regiones,
        'inmuebles': inmuebles
    }
    
    return render (req, 'index.html', context)


def filtrar_inmuebles(region_cod, comuna_cod,palabra):
    # Caso 1: comuna_cod != ''
    # Caso 2: comuna_cod == '' and region_cod != ''
    # Caso 3: comuna_cod == '' and region_cod == ''
    if comuna_cod != '':
        comuna = Comuna.objects.get(cod=comuna_cod)
        
        return Inmueble.objects.filter(comuna= comuna)
    # elif comuna_cod == '' and region_cod != '':
    #     return Inmueble.objects.filter()
    
    inmuebles = Inmueble.objects.all()
    
    return inmuebles


#esta funciona para filtrar las propiedades que pertenecen al usuario
@login_required
def profile (req):
    id_usuario = req.user.id
    propiedades = Inmueble.objects.filter(propietario_id = id_usuario)
    context ={
        'propiedades' : propiedades
    }
    return render (req, 'profile.html', context)

# @login_required
# def profile(req):
#     user=req.usermis_inmuebles= None
#     if user.user_profile.rol == 'arrendador':
#         mis_inmuebles = user.inmuebles.all()
#     elif user.user_profile.rol == 'arrendatario':
#         pass
    
#     context ={
#         'mis_inmuebles' : mis_inmuebles
#     }
#     return render(req, 'profile.html', context)
    



@login_required
def edit_user(req):
    # 1 Obtengo el usuario actual
    current_user = req.user
    #llamo  la funcion para editar el usuario
    if req.POST ['telefono'].strip !='':
        #editar lo trailing whitespaces strip
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'],
            req.POST['rol'],
            req.POST['telefono']
        )
        
    else:
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'],
            req.POST['rol'],
        )
    messages.success(req, '¡Usuario actualizado!')
    return redirect('/')
            
    # forma desde la vista
    
# def change_password(req):
# # 1 recibo los datos del formulario
#     password= req.POST['password']
#     pass_repeat= req.POST['pass-repeat']
# # 2 Valido que ambas contraseñas coincidad
#     if password != pass_repeat:
#         messages.error(req, 'Las contraseñas no coinciden')
#         return redirect('/accounts/profile')
# # 3 actualizamos la contraseña
#     req.user.set_password(password)
#     req.user.save()
# # 4 se arroja un mensaje de exito al usuario
#     messages.success(req, 'Contraseña actualizada')
#     return redirect('/accounts/profile')
    
#forma desde un servicio
def change_password(req): 
    password= req.POST['password']
    pass_repeat= req.POST['pass_repeat']
    cambio_pass(req, password, pass_repeat)
    return redirect ('/accounts/profile')

def add_propiedad(req):
    if req.method == 'POST':
        propietario_rut = req.user
        nombre = req.POST['nombre']
        descripcion = req.POST['descripcion']
        M2_construidos = int(req.POST['M2_construidos'])
        M2_totales_terreno = int(req.POST['M2_totales_terreno'])
        cant_estacionamientos =int(req.POST['cant_estacionamientos'])
        cant_habitaciones =int(req.POST['cant_habitaciones'])
        cant_banos = int(req.POST['cant_banos'])
        direccion = req.POST['direccion']
        tipo_vivienda = req.POST['tipo_vivienda']
        precio_mensual = int(req.POST['precio_mensual'])
        comuna_cod = str(req.POST['comuna'])
        crear_inmueble(
            nombre, descripcion, M2_construidos, M2_totales_terreno, cant_estacionamientos, cant_habitaciones, cant_banos, direccion, precio_mensual, tipo_vivienda, comuna_cod, propietario_rut)
        return redirect ('profile')
    else:
        return render (req, 'add_propiedad.html')
    
    
    # test solicita que el usuario requiere no estar autentificado
def usuario_no_autentificado(user):
    # retorna un usuario no  autentificado
    return not user.is_authenticated

@user_passes_test(usuario_no_autentificado) # eñ 
def register(req):
    if req.method == 'POST':
        rut = req.POST ['rut']
        first_name = req.POST ['first_name']
        last_name = req.POST ['last_name']
        email = req.POST ['email']
        password = req.POST['password']
        pass_confirm = req.POST ['pass_confirm']
        direccion = req.POST ['direccion']
        telefono = req.POST ['telefono']
        crear_user(
            req,rut,first_name ,last_name, email, password, pass_confirm, direccion, telefono)
        return redirect('/accounts/login')
        
    else:
        return render(req, 'register.html')
        
