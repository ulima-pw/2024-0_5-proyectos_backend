from django.urls import path

from .views import verEquiposEndpoint, verEquiposPathParametersEndpoint

urlpatterns = [
    path("ver-equipos", verEquiposEndpoint),
    path("ver-equipos-path/<str:filtro>", verEquiposPathParametersEndpoint)
]