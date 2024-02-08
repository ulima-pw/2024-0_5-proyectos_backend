from django.urls import path

from .views import verEquiposEndpoint, verEquiposPathParametersEndpoint
from .views import loginEndpoint, loginPostEndpoint
from .views import loginPostJsonEndpoint

urlpatterns = [
    path("ver-equipos", verEquiposEndpoint),
    path("ver-equipos-path/<str:filtro>", verEquiposPathParametersEndpoint),
    path("login/<str:username>/<str:password>", loginEndpoint),
    path("login", loginPostEndpoint),
    path("login-json", loginPostJsonEndpoint)
]