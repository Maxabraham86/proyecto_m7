from main.models import UserProfile, Comuna, Inmueble
from django.contrib.auth.models import User




def crear_user(rut: str,first_name:str ,last_name:str, email:str, password:str, direccion:str, telefono:str):
    user = User.objects.create_user(
            username= rut,
            first_name = first_name,
            last_name= last_name,
            email= email,
            password=  password
        )
    UserProfile.objects.create(
            user=user,
            direccion=direccion,
            telefono =telefono,
        )



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
    pass



def editar_user(*args):
    pass

def eliminar_user(rut:str):
    eliminar = User.object.get(username=rut)
    eliminar.delete()