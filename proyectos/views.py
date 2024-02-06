from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

usuarios = """
[
    {
        "username" : "usuario1",
        "password" : "123"
    },
    {
        "username" : "usuario2",
        "password" : "abc"
    },
    {
        "username" : "usuario3",
        "password" : "aaa"
    }
]
"""

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


# Path: /proyectos/login GET
# Response:
# {
#    "msg" : "" // Login Correcto
# }

# {
#    "msg" : "Error en login" // Login Incorrecto
# }

def loginEndpoint(request, username, password):
    if request.method == "GET":
        # Peticion GET
        listaUsuarios = json.loads(usuarios)
        listaUsuariosFiltrada = list(
            filter( 
                lambda x : x["username"] == username and x["password"] == password,
                listaUsuarios
            )
        )

        if len(listaUsuariosFiltrada) > 0 :
            respuesta = {
                "msg" : ""
            }
            return HttpResponse(json.dumps(respuesta))
        else :
            respuesta = {
                "msg" : "Error en el login"
            }
            return HttpResponse(json.dumps(respuesta))

# Path: /proyectos/login POST

@csrf_exempt
def loginPostEndpoint(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        listaUsuarios = json.loads(usuarios)
        listaUsuariosFiltrada = list(
            filter( 
                lambda x : x["username"] == username and x["password"] == password,
                listaUsuarios
            )
        )

        if len(listaUsuariosFiltrada) > 0 :
            respuesta = {
                "msg" : ""
            }
            return HttpResponse(json.dumps(respuesta))
        else :
            respuesta = {
                "msg" : "Error en el login"
            }
            return HttpResponse(json.dumps(respuesta))


