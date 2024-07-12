from django.core.management.base import BaseCommand
from django.contrib.auth. models import User
import csv
from main.models import Inmueble, Comuna, User
from main.services import crear_inmueble

class Command(BaseCommand):
   def handle (self, *args, **kwargs):
        archivo = open('data/inmuebles.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=',')
        next(reader) 
    
    
        for fila in reader:
            try:
                crear_inmueble(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[9],fila[8],fila[10],fila[11])
            except Comuna.DoesNotExist:
                print (f'Fallo de comuna {fila[10]}')
        
        #     nombre = fila[0],
        #     descripcion = fila[1],                    
        #     M2_construidos = fila[2],
        #     M2_totales_terreno = fila[3],
        #     cant_estacionamientos = fila[4],
        #     cant_habitaciones = fila[5],
        #     cant_banos = fila[6],
        #     direccion = fila[7],
        #     tipo_vivienda = fila[8],
        #     precio_mensual =fila[9],
        #     comuna_cod = fila[10],
        #     propietario_rut = fila[11]
        # )    
            # crear_inmueble(nombre, descripcion, M2_construidos, M2_totales_terreno,cant_estacionamientos, cant_habitaciones, cant_banos, direccion, precio_mensual, tipo_vivienda, comuna_cod, propietario_rut)