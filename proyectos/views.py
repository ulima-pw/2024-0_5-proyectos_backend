from django.shortcuts import render
from django.http import HttpResponse

equipos = """
[
    {
        "nombre" : "Equipo 1",
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
    return HttpResponse(equipos)
