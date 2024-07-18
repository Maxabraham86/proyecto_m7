from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from main.services import editar_user_sin_password
from django.contrib.auth.models import User
from django.contrib import messages

#from django.contrib.auth import user
# Create your views here.
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
    if req.POST ['telefono'] !='':
        #editar lo trailing whitespaces strip
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['direccion'],
            req.POST['email'],
            req.POST['telefono']
        )
        
    else:
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['direccion'],
            req.POST['email'],
            
        )
    messages.success(req, '¡Usuario actualizado!')
    return redirect('/')
            
    
def change_password(req):
    
    #1 recibo los datos del formulario
    password= req.POST['password']
    pass_repeat= req.POST['pass-repeat']
    # 2 Valido que ambas contraseñas coincidad
    
    if password != pass_repeat:
        messages.error(req, 'Las contraseñas no coinciden')
        return redirect('/accounts/profile')
    #3 actualizamos la contraseña
    req.user.set_password(password)
    req.user.save()
    
    # 4 se arroja un mensaje de exito al usuario
    messages.success(req, 'Contraseña actualizada')
    return redirect('/accounts/profile')
    




