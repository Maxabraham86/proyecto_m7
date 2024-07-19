from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from main.services import editar_user_sin_password, cambio_pass, crear_inmueble
from django.contrib.auth.models import User
from django.contrib import messages
from django import template
#from django.contrib.auth import user

def success(req):
    return render(req,'exito.html')

def form_test(req):
    return render (req,'form_test.html')

@login_required
def index(req):
    return render (req, 'index.html')


@login_required
def profile (req):
    return render (req, 'profile.html')

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
    
#     #1 recibo los datos del formulario
#     password= req.POST['password']
#     pass_repeat= req.POST['pass-repeat']
#     # 2 Valido que ambas contraseñas coincidad
    
#     if password != pass_repeat:
#         messages.error(req, 'Las contraseñas no coinciden')
#         return redirect('/accounts/profile')
#     #3 actualizamos la contraseña
#     req.user.set_password(password)
#     req.user.save()
    
#     # 4 se arroja un mensaje de exito al usuario
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