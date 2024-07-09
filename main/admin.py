from django.contrib import admin
from main.models import Comuna, Inmueble, UserProfile
# Register your models here.

class ComunaAdmin(admin.ModelAdmin):
    pass

class InmuebleAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    pass



admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Inmueble, ComunaAdmin)
admin.site.register(UserProfile, ComunaAdmin)