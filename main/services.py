from django.contrib.auth.models import User
from main.models import UserProfile, Comuna, Inmueble, Region
from django.db.utils import IntegrityError
from django.db.models import Q 
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages

def crear_user(req,rut: str,first_name:str ,last_name:str, email:str, password:str, pass_confirm:str, direccion:str, telefono:str =None)->[bool, str]:
        #validamos que el password coincida
    if password !=pass_confirm:
        return False, 'las contraseñas no coinciden'
    
    #2 creamos objeto user
    try:
        user = User.objects.create_user(
            username= rut,
            first_name = first_name,
            last_name= last_name,
            email= email,
            password=  password,
    )
    except IntegrityError:
        return False, 'Rut duplicado'
    #3 creamos el UserProfile
    
    UserProfile.objects.create(
        user=user,
        direccion=direccion,
        telefono =telefono,
    )
    #4 si todo sale bien retornamos True
    messages.success(req, 'Usuario creado con exito, ingrese a su sesion')
    return True

def editar_user(username: str,first_name:str ,last_name:str, email:str, password:str, direccion:str, telefono:str =None):
    user=User.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password = (password)
    user.save()

    user_profile = UserProfile.objects.get(user=user)
    user_profile.direccion = direccion
    user_profile.telefono = telefono
    user_profile.save()


def crear_inmueble(nombre:str, descripcion:str, M2_construidos:int, M2_totales_terreno:int, cant_estacionamientos:int, cant_habitaciones:int, cant_banos:int, direccion:str, precio_mensual:int, tipo_vivienda:str, comuna_cod :str, propietario_rut:str):
    comuna = Comuna.objects.get(cod=comuna_cod)
    propietario = User.objects.get(username=propietario_rut)
    Inmueble.objects.create(
        nombre = nombre,
        descripcion = descripcion,
        M2_construidos = M2_construidos,
        M2_totales_terreno = M2_totales_terreno,
        cant_estacionamientos = cant_estacionamientos,
        cant_habitaciones = cant_habitaciones,
        cant_banos = cant_banos,
        direccion = direccion,
        tipo_vivienda = tipo_vivienda,
        precio_mensual = precio_mensual,
        comuna = comuna,
        propietario = propietario
    )

def editar_inmueble(inmueble_id:int, nombre:str, descripcion:str, M2_construidos:int, M2_totales_terreno:int, cant_estacionamientos:int, cant_habitaciones:int, cant_banos:int, direccion:str, precio_mensual:int, tipo_vivienda:str, comuna:str, rut_propietario:str):
    inmueble=Inmueble.objects.get(id=inmueble_id)
    comuna = Comuna.objects.get(nombre=comuna)
    propietario = User.objects.get(username=rut_propietario)
    inmueble.nombre = nombre          
    inmueble.descripcion = descripcion                           
    inmueble.M2_construidos = M2_construidos
    inmueble.M2_totales_terreno = M2_totales_terreno
    inmueble.cant_estacionamientos = cant_estacionamientos
    inmueble.cant_habitaciones = cant_habitaciones
    inmueble.cant_banos = cant_banos
    inmueble.direccion = direccion
    inmueble.tipo_vivienda = tipo_vivienda
    inmueble.precio_mensual = precio_mensual
    inmueble.comuna = comuna
    inmueble.propietario = propietario
    inmueble.save()

def eliminar_inmueble(inmueble_id):
    eliminar=Inmueble.objects.get(id=inmueble_id)
    eliminar.delete()




def eliminar_user(rut:str):
    eliminar = User.object.get(username=rut)
    eliminar.delete()


    #esta funciona  
# def obtener_inmuebles_comunas(filtro):
#     if filtro is None:
#         return Inmueble.objects.all().order_by('comuna')

#     #si llegamos acá, significa que Si hay un filtro
#     return Inmueble.objects.filter(nombre__icontains=filtro).order_by('comuna')



def obtener_inmuebles_comunas(filtro):
    if filtro is None:
        return Inmueble.objects.all().order_by('comuna')

    #si llegamos acá, significa que Si hay un filtro
    return Inmueble.objects.filter(Q(nombre__icontains=filtro) | Q ( descripcion__icontains=filtro)).order_by('comuna')




def obtener_inmuebles_regiones1(filtro):
    if filtro is None:
        
        consulta ='select * from main_inmueble as I join main_comuna as C on I.comuna_id = C.cod join main_region as R on C.region_id = R.cod order by R.cod'
        
        return Inmueble.objects.raw(consulta)

    #si llegamos acá, significa que Si hay un filtro
    #return Inmueble.objects.filter(nombre__icontains=filtro).order_by('region')


def obtener_inmuebles_regiones(filtro):
    consulta ='''select I.nombre, I.descripcion, R.nombre as region from main_inmueble as I join main_comuna as C on I.comuna_id = C.cod join main_region as R on C.region_id = R.cod order by R.cod'''
    if filtro is not None:
        consulta =f'''select I.nombre, I.descripcion, R.nombre as region from main_inmueble as I join main_comuna as C on I.comuna_id = C.cod join main_region as R on C.region_id = R.cod where I.nombre like '%{filtro}%' or I.descripcion like '%{filtro}%' order by R.cod'''    
    cursor= connection.cursor()
    cursor.execute(consulta)
    registros = cursor.fetchall()    
    return registros


def editar_user_sin_password(username, first_name, last_name, email, direccion,rol, telefono=None) -> list[bool, str]:
    # 1. Nos traemos el 'user' y modificamos sus datos
    user = User.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    # 2. Nos traemos el 'user_profile' y modificamos sus datos
    user_profile = UserProfile.objects.get(user=user)
    user_profile.direccion = direccion
    user_profile.telefono = telefono
    user_profile.rol = rol
    user_profile.save()



def cambio_pass(req, password, pass_repeat):
    if password != pass_repeat:
        messages.warning(req,' la contraseña no coincide')
        return 
    req.user.set_password(password)
    req.user.save()
    messages.success(req, 'Contraseña actualizada exitosamente')
    