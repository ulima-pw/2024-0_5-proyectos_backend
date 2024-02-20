from django.urls import path

from .views import verEquiposEndpoint
from .views import loginPostJsonEndpoint
from .views import registrarEquipo
from .views import eliminarEquipo
from .views import verEquipo
from .views import verCursosDisponibles
from .resources.equipo import equipoResource, equipoInfoResource

urlpatterns = [
    path("ver-equipos", verEquiposEndpoint),
    #path("ver-equipos-path/<str:filtro>", verEquiposPathParametersEndpoint),
    #path("login/<str:username>/<str:password>", loginEndpoint),
    #path("login", loginPostEndpoint),
    path("login-json", loginPostJsonEndpoint),
    path("eliminar-equipo", eliminarEquipo),
    path("ver-equipo", verEquipo),
    path("ver-cursos", verCursosDisponibles),
    path("equipo", equipoResource),
    path("equipo/<str:equipoid>", equipoInfoResource)
]