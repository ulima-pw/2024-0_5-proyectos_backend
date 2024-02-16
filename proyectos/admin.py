from django.contrib import admin
from .models import Usuario, Equipo, Integrante, Curso, EquipoXCurso

class EquipoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "anho", "estado"]

class IntegranteAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "equipo"]

class EquipoXCursoAdmin(admin.ModelAdmin):
    list_display = ["equipo", "curso"]

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Curso)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Integrante, IntegranteAdmin)
admin.site.register(EquipoXCurso, EquipoXCursoAdmin)
