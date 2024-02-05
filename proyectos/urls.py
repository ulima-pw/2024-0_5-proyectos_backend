from django.urls import path

from .views import verEquiposEndpoint

urlpatterns = [
    path("ver-equipos", verEquiposEndpoint)
]