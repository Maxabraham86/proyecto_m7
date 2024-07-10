
from django.core.management.base import BaseCommand
from main.models import UserProfile, Comuna, Inmueble, Solicitud
from main.services import crear_user
class Command(BaseCommand):
        

    def handle (self, *args, **kwargs):

        #funciona con la funcion que ya funcionaba 
        #c=crear_user('11111111-1', 'Juan', 'Marino', 'aaa@bbb.ccc', '1234', 'calle falsa 123', '123456789')
        
        crear_user('1234567-8', 'Pedro', 'Picapiedra', 'aaa@bbb.ccc', '1234', '1234' , 'Av Rocadira 48')


        # inmueble4= Inmueble.objects.create(
        #     nombre='Bolsos Cerrado',
        #     descripcion ='Gran casa en hermosa y apasible villa rural',
        #     M2_construidos= 800,
        #     M2_totales_terreno=1000,
        #     direccion='ls Comarca 24',
        #     comuna =comuna4,
        #     tipo_vivienda = 'par',
        #     precio_mensual= 1500000,
        #     cant_estacionamientos =8,
        #     cant_habitacion =12,
        #     cant_banos=5
        # )
        