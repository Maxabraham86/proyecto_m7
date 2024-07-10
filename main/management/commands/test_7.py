
from django.core.management.base import BaseCommand
from main.models import UserProfile, Comuna, Inmueble, Solicitud
from main.services import crear_user, editar_user, crear_inmueble, editar_inmueble
class Command(BaseCommand):
        

    def handle (self, *args, **kwargs):

        #funciona con la funcion que ya funcionaba 
        #c=crear_user('11111111-1', 'Juan', 'Marino', 'aaa@bbb.ccc', '1234', 'calle falsa 123', '123456789')
        
        #crear_user('1234567-8', 'Pedro', 'Picapiedra', 'aaa@bbb.ccc', '1234', '1234' , 'Av Rocadura 48')
        #crear_user('111222333-4', 'Sandro', 'de Lucia', 'aaa@bbb.ccc', '1234', '1234' , 'la alhambra 333')
        #crear_user('112233445-5', 'Octubre', 'Capilla', 'aaa@bbb.ccc', '1234', '1234' , 'el milagro 28')
        
        #editar_user('1234567-8', 'PePe', 'Picapiedra', 'ddd@eee.fff', '4321', 'El granito 22')

    
        # crear_inmueble(
        #     nombre='Bolsón Cerrado',
        #     descripcion ='Gran casa en hermosa y apasible villa rural',
        #     M2_construidos= 800,
        #     M2_totales_terreno=1000,
        #     direccion='la Comarca 24',
        #     precio_mensual= 1500000,
        #     tipo_vivienda = 'par',
        #     cant_estacionamientos =8,
        #     cant_habitacion =12,
        #     cant_banos=5,
        #     comuna = 'viña del mar',
        #     propietario= '111222333-4'
        # )

        #crear_inmueble ('casa de lucia', 'casa en la que vive de lucia', 150,250, 3,3,2,'granada 338', 600000, 'casa','viña del mar', '111222333-4' ) 
        #crear_inmueble ('depto de Betty', 'departamento de Betty Boop', 80,80, 1,2,2,'granada 338', 200000, 'depto','valdivia', '11111111-1' )
        
        #crear_inmueble('Casa Grande en Villarrica', 'Esta es la descripcion de propiedad', 150, 250, 3, 5, 4, 'volcan 22', 700000, 'par', 'villarrica', '112233445-5')
        
        editar_inmueble(1,'Parcela en Villarrica', 'propiedad ideal para relajarse y cuidar animales', 150, 250, 3, 5, 4, 'volcan 22', 700000, 'par', 'villarrica', '112233445-5')
        
        return 'okidoki'