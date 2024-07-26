from django.urls import path
from main.views import form_test, index, profile, edit_user, change_password, add_propiedad, register, prueba
from django.contrib.auth import views as auth_views


urlpatterns =[
    path ('', index, name='index'),
    path('form_test/', form_test, name = 'form_test'),
    path('accounts/profile/', profile, name='profile'),
    path('edit-user/', edit_user , name ='edit_user'),
    path('accounts/change-pass/', change_password, name ='change_password' ),
    path('add-propiedad/', add_propiedad, name = "add_propiedad"),
    path('register/', register, name ='register'),
    path('prueba/', prueba, name ='prueba'),
    
]