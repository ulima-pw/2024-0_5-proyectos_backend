from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from proyectos.models import Equipo, Usuario

def verEquiposEndpoint(request):
    if request.method == "GET":
        # Es una peticion de tipo GET
        nombreFiltro = request.GET.get("nombre") # Obtenemos query parameter nombre
        anhoFiltro = request.GET.get("anho")

        if nombreFiltro == "" and anhoFiltro == "-":
            # No hay que filtrar nada
            listaEquiposFiltrada = Equipo.objects.all()
        else:
            # Si ha enviado filtro
            listaEquiposFiltrada = Equipo.objects.filter(nombre__contains=nombreFiltro, anho=anhoFiltro)

        dataResponse = []
        for equipo in listaEquiposFiltrada:
            dataResponse.append({
                "nombre" : equipo.nombre,
                "integrantes" : []
            })

        return HttpResponse(json.dumps(dataResponse))

# def verEquiposPathParametersEndpoint(request, filtro):
#     if request.method == "GET":
#         # Es una peticion de tipo GET
#         nombreFiltro = filtro # Obtenemos path parameter filtro

#         listaEquipos = json.loads(equipos)
#         listaEquiposFiltrada = list(
#             filter(
#                 lambda x : x["nombre"].lower() == nombreFiltro, 
#                 listaEquipos
#             )
#         )
#         return HttpResponse(json.dumps(listaEquiposFiltrada))
#     return HttpResponse(equipos)


# Path: /proyectos/login GET
# Response:
# {
#    "msg" : "" // Login Correcto
# }

# {
#    "msg" : "Error en login" // Login Incorrecto
# }
# def loginEndpoint(request, username, password):
#     if request.method == "GET":
#         # Peticion GET
#         listaUsuarios = json.loads(usuarios)
#         listaUsuariosFiltrada = list(
#             filter( 
#                 lambda x : x["username"] == username and x["password"] == password,
#                 listaUsuarios
#             )
#         )

#         if len(listaUsuariosFiltrada) > 0 :
#             respuesta = {
#                 "msg" : ""
#             }
#             return HttpResponse(json.dumps(respuesta))
#         else :
#             respuesta = {
#                 "msg" : "Error en el login"
#             }
#             return HttpResponse(json.dumps(respuesta))

# Path: /proyectos/login POST
# @csrf_exempt
# def loginPostEndpoint(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         listaUsuarios = json.loads(usuarios)
#         listaUsuariosFiltrada = list(
#             filter( 
#                 lambda x : x["username"] == username and x["password"] == password,
#                 listaUsuarios
#             )
#         )

#         if len(listaUsuariosFiltrada) > 0 :
#             respuesta = {
#                 "msg" : ""
#             }
#             return HttpResponse(json.dumps(respuesta))
#         else :
#             respuesta = {
#                 "msg" : "Error en el login"
#             }
#             return HttpResponse(json.dumps(respuesta))

#Path: /login-json
#Request:
#{
#    "username" : "usuario1",
#    "password" : "123"
#}
#Response:
#{
#   "msg": ""
#}
@csrf_exempt
def loginPostJsonEndpoint(request):
    if request.method == "POST":
        data = request.body
        usernameData = json.loads(data)

        username = usernameData["username"]
        password = usernameData["password"]

        # Interactuamos con la bd mediante el modelo (Query)
        listaUsuariosFiltrada = Usuario.objects.filter(
            username=username, password=password
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


# Path: /proyectos/equipo POST
# Description: Este endpoint se encargara de registrar un nuevo equipo
# Request:
# {
#    "nombre" : "Equipo A",
#    "anho" : "2024"
# }
# Response
# {
#    "msg" : ""  | "msg" : "Hubo un error bla bla..."
# }
@csrf_exempt
def registrarEquipo(request):
    if request.method == "POST":
        data = request.body
        equipoDict = json.loads(data)

        if equipoDict["nombre"] == "" and equipoDict["anho"] == "":
            errorDict = {
                "msg" : "Debe ingresar un nombre de equipo"
            }
            return HttpResponse(json.dumps(errorDict))

        equipo = Equipo(
            nombre=equipoDict["nombre"], 
            anho=equipoDict["anho"], 
            estado="A"
        )
        equipo.save()

        respDict = {
            "msg" : ""
        }
        return HttpResponse(json.dumps(respDict))



