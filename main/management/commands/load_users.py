from django.core.management.base import BaseCommand
import csv
from main.models import User
from main.services import crear_user

class Command(BaseCommand):
   def handle (self, *args, **kwargs):
      archivo = open('data/users.csv', encoding='utf-8')
      reader = csv.reader(archivo, delimiter=';')
      next(reader)  # Saltar la cabecera
        
      for fila in reader:
        username = fila[0]
        first_name = fila[1]
        last_name = fila[2]
        email = fila[3]
        password = fila[4]
        pass_confirm = fila[5]
        direccion = fila[6]
          
          
        crear_user(username, first_name, last_name, email, password, pass_confirm, direccion)