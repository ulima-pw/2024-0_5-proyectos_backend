from django.contrib import admin
from .models import Usuario, Equipo, Integrante

class EquipoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "anho", "estado"]

class IntegranteAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "equipo"]

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Integrante, IntegranteAdmin)
