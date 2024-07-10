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

def crear_user(rut: str,first_name:str ,last_name:str, email:str, password:str, pass_confirm:str, direccion:str, telefono:str =None)->bool:
        #validamos que el password coincida
    if password !=pass_confirm:
        return False
    #2 creamos objeto user
    user = User.objects.create_user(
        username= rut,
        first_name = first_name,
        last_name= last_name,
        email= email,
        password=  password,
        
    )
    #3 creamos el UserProfile
    
    UserProfile.objects.create(
        user=user,
        direccion=direccion,
        telefono =telefono,
    )

    #4 si todo sale bien retornamos True
    return True

def crear_inmueble(nombre, descripcion,direccion, M2_construidos, M2_totales_terreno, tipo_vivienda, precio_mensual,cant_estacionamientos,cant_habitacion,cant_banos, comuna_id, propietario_id ):
#inmueble1= Inmueble.objects.create( 
    
        comuna = Comuna.objects.get(id=comuna_id)
        proprietario = User.objectos.get (id_propietario)
        inmueble=Inmueble(
            nombre= nombre,
            descripcion =descripcion,
            M2_construidos= M2_construidos,
            M2_totales_terreno= M2_totales_terreno,
            direccion=direccion,
            comuna =comuna,
            tipo_vivienda = tipo_vivienda,
            precio_mensual= precio_mensual,
            cant_estacionamientos =cant_estacionamientos,
            cant_habitacion =cant_habitacion,
            cant_banos=cant_banos
        )

def editar_inmueble(*args):
    pass

def eliminar_inmueble(inmueble_id):
    eliminar=Inmueble.objects.get()
    eliminar.delete()



def editar_user(*args):
    pass

def eliminar_user(rut:str):
    eliminar = User.object.get(username=rut)
    eliminar.delete()