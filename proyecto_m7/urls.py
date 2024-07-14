from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
#from main.views import success
#from main.views import LoginViewPropia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include ('django.contrib.auth.urls'),name='login'),
    path('', include('main.urls'))
    
    
    #path('accounts/login/', LoginViewPropia.as_view()),
]
