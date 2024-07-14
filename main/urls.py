from django.urls import path
from main.views import form_test, index
from django.contrib.auth import views as auth_views


urlpatterns =[
    path ('', index, name='index'),
    path('form_test/', form_test, name = 'form_test'),
    #path('flan/<id>/', detalleFlan, name="flan id"),
    
]