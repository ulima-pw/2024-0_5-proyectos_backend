from django.shortcuts import render
from django.http import HttpResponse
import json

equipos = """
[
    {
        "nombre" : "Equipo1",
        "integrantes" : [
            {
                "nombre" : "N1",
                "codigo" : "20202323"
            },
            {
                "nombre" : "N2",
                "codigo" : "20224533"
            }
        ]
    },
    {
        "nombre" : "Equipo 2",
        "integrantes" : [
            {
                "nombre" : "N3",
                "codigo" : "20202323"
            },
            {
                "nombre" : "N4",
                "codigo" : "20224533"
            }
        ]
    },
    {
        "nombre" : "Equipo 3",
        "integrantes" : [
            {
                "nombre" : "N5",
                "codigo" : "20220022"
            },
            {
                "nombre" : "N6",
                "codigo" : "20192343"
            }
        ]
    }
]
"""

def verEquiposEndpoint(request):
    if request.method == "GET":
        # Es una peticion de tipo GET
        nombreFiltro = request.GET.get("nombre") # Obtenemos query parameter nombre

        ##def filtro(equipo) :
        ##    return equipo["nombre"].lower() == nombreFiltro

        listaEquipos = json.loads(equipos)
        listaEquiposFiltrada = list(
            filter(
                lambda x : x["nombre"].lower() == nombreFiltro, 
                listaEquipos
            )
        )
        return HttpResponse(json.dumps(listaEquiposFiltrada))


    return HttpResponse(equipos)

def verEquiposPathParametersEndpoint(request, filtro):
    if request.method == "GET":
        # Es una peticion de tipo GET
        nombreFiltro = filtro # Obtenemos path parameter filtro

        listaEquipos = json.loads(equipos)
        listaEquiposFiltrada = list(
            filter(
                lambda x : x["nombre"].lower() == nombreFiltro, 
                listaEquipos
            )
        )
        return HttpResponse(json.dumps(listaEquiposFiltrada))


    return HttpResponse(equipos)
