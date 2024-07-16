from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from main.services import editar_user_sin_password
from django.contrib.auth.models import User
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
    print(req.POST)
    usuario = req.user
    first_name = req.POST['first_name']
    last_name = req.POST['last_name']
    direccion=req.POST['direccion']
    email =req.POST['email']
    telefono = req.POST['telefono']
    editar_user_sin_password(usuario,first_name, last_name, email, direccion, telefono )
    return HttpResponse ('Funciona')




#username, first_name, last_name, email, direccion, telefono=None