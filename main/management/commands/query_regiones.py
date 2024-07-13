from django.core.management.base import BaseCommand
import csv
from main.services import obtener_inmuebles_regiones

from main.models import Inmueble



class Command(BaseCommand):
        
        def add_arguments(self, parser):
            # positional arguments
            parser.add_argument('-f','--f', type=str, nargs='+')
        def handle (self, *args, **kwargs):
            archivo = open('data/inmuebles_regiones.txt', 'w', encoding='utf-8')
        
            filtro=  None
            if 'f' in kwargs.keys() and kwargs['f'] is not None:
                filtro = kwargs['f'][0]
            inmuebles = obtener_inmuebles_regiones(filtro)
                
                #inmuebles=Inmueble.objects.all()    
                
            # if filtro:
            #     inmuebles =inmuebles.filter(nombre__icontains=filtro)
                
            for inmueble in inmuebles:
                print(inmueble)
                linea = f'{inmueble[0]} \t{inmueble[1]}\t{inmueble[2]}'
                archivo.write(linea)
                archivo.write('\n')
                print(linea)
            archivo.close()
