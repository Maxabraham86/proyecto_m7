from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from inmueble.views import nuevo_inmueble, crear_inmueble, editar_inmueble, eliminar_inmueble

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include ('django.contrib.auth.urls'),name='login'),
    path('', include('main.urls')),
    path ('inmueble/nuevo/', nuevo_inmueble, name = 'nuevo_inmueble'),
    path('inmueble/crear/', crear_inmueble, name='crear_inmueble'),
    path('inmueble/editar/<id>', editar_inmueble, name='editar_inmueble'),
    path('inmueble/eliminar/<id>', eliminar_inmueble, name='eliminar_inmueble'),
    
]
