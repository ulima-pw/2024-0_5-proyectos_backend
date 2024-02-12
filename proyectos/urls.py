from django.urls import path

from .views import verEquiposEndpoint
from .views import loginPostJsonEndpoint
from .views import registrarEquipo

urlpatterns = [
    path("ver-equipos", verEquiposEndpoint),
    #path("ver-equipos-path/<str:filtro>", verEquiposPathParametersEndpoint),
    #path("login/<str:username>/<str:password>", loginEndpoint),
    #path("login", loginPostEndpoint),
    path("login-json", loginPostJsonEndpoint),
    path("equipo", registrarEquipo)
]