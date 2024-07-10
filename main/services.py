from django.contrib.auth.models import User
from main.models import UserProfile, Comuna, Inmueble
from django.db.utils import IntegrityError

#este ya funciona

# def crear_user(rut: str,first_name:str ,last_name:str, email:str, password:str, direccion:str, telefono:str):
#     user = User.objects.create_user(
#             username= rut,
#             first_name = first_name,
#             last_name= last_name,
#             email= email,
#             password=  password
#         )
#     UserProfile.objects.create(
#             user=user,
#             direccion=direccion,
#             telefono =telefono,
#         )


#metodo trabajado en clases

def crear_user(rut: str,first_name:str ,last_name:str, email:str, password:str, pass_confirm:str, direccion:str, telefono:str =None)->[bool, str]:
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


# def crear_inmueble(nombre, descripcion,direccion, M2_construidos, M2_totales_terreno, tipo_vivienda, precio_mensual,cant_estacionamientos,cant_habitacion,cant_banos, comuna_id, propietario_id ):
# #inmueble1= Inmueble.objects.create( 
    
#         comuna = Comuna.objects.get(id=comuna_id)
#         proprietario = User.objectos.get(id_propietario)
#         inmueble=Inmueble(
#             nombre= nombre,
#             descripcion =descripcion,
#             M2_construidos= M2_construidos,
#             M2_totales_terreno= M2_totales_terreno,
#             direccion=direccion,
#             comuna =comuna,
#             tipo_vivienda = tipo_vivienda,
#             precio_mensual= precio_mensual,
#             cant_estacionamientos =cant_estacionamientos,
#             cant_habitacion =cant_habitacion,
#             cant_banos=cant_banos,
#             propietario=propietario
#         )

def crear_inmueble(nombre:str, descripcion:str, M2_construidos:int, M2_totales_terreno:int, cant_estacionamientos:int, cant_habitaciones:int, cant_banos:int, direccion:str, precio_mensual:int, tipo_vivienda:str, comuna:str, rut_propietario:str):
    comuna = Comuna.objects.get(nombre=comuna)
    propietario = User.objects.get(username=rut_propietario)
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
    eliminar=Inmueble.objects.get()
    eliminar.delete()




def eliminar_user(rut:str):
    eliminar = User.object.get(username=rut)
    eliminar.delete()