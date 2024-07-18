from django.urls import path
from main.views import form_test, index, profile, edit_user, change_password
from django.contrib.auth import views as auth_views


urlpatterns =[
    path ('', index, name='index'),
    path('form_test/', form_test, name = 'form_test'),
    #path('flan/<id>/', detalleFlan, name="flan id"),
    path('accounts/profile/', profile, name='profile'),
    path('edit-user/', edit_user , name ='edit_user'),
    path('accounts/change-pass/', change_password, name ='change_password' )
]