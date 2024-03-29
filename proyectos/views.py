from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from proyectos.models import Equipo, Usuario, Integrante, Curso, EquipoXCurso

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
            listaIntegrantesQuerySet = Integrante.objects.filter(equipo_id = equipo.pk) # QuerySet
            listaIntegrantes = list(listaIntegrantesQuerySet.values())
            print('1 +++++++++++++++++++++++++++++++++++++')
            print(listaIntegrantesQuerySet)
            print(listaIntegrantes)
            dataResponse.append({
                "id" : equipo.pk,
                "nombre" : equipo.nombre,
                "integrantes" : listaIntegrantes
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
#    "anho" : "2024",
#    "integrantes" : [ ... ],
#    "cursos" : [1,5]
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

        if equipoDict["nombre"] == "" or equipoDict["anho"] == "":
            errorDict = {
                "msg" : "Debe ingresar los datos completo de equipo"
            }
            return HttpResponse(json.dumps(errorDict))
    
        # insert equipo
        equipo = Equipo(
            nombre=equipoDict["nombre"], 
            anho=equipoDict["anho"], 
            estado="A"
        )
        equipo.save()
        
        # Agregando integrantes
        integrantes = equipoDict['integrantes']  
        for d in integrantes:
            integrante = Integrante(
                codigo = d['codigo'],
                nombre = d['nombre'],
                equipo = equipo
            )
            integrante.save()

        # Relacionando con cursos
        cursos = equipoDict['cursos']
        for cursoId in cursos:
            curso = Curso.objects.get(pk=cursoId)
            equipoXCurso = EquipoXCurso(
                curso = curso,
                equipo = equipo
            )
            equipoXCurso.save()


        respDict = {
            "msg" : ""
        }
        return HttpResponse(json.dumps(respDict))


# Path: /proyectos/eliminar-equipo?id=3 GET
# Request: Query parameter
# Reponse:
# {
#    "msg" : "" | "msg" : "Error eliminando equipo"
# }
def eliminarEquipo(request):
    if request.method == "GET":
        equipoId = request.GET.get("id")

        if equipoId == "":
            errorDict = {
                "msg" : "Debe enviar un id de equipo"
            }
            return HttpResponse(json.dumps(errorDict))
        
        try:
            equipo = Equipo.objects.get(pk=equipoId)
        except:
            errorDict = {
                "msg" : "Debe enviar un id de equipo existente "
            }
            return HttpResponse(json.dumps(errorDict))
            
        equipo.delete()

        msgDict = {
            "msg" : ""
        }
        return HttpResponse(json.dumps(msgDict))

# Path /proyectos/ver-equipo?id=1 GET
# Request: Query parameter
# Response:
# {
#    "id" : 1,
#    "nombre" : "23232",
#    "anho" : "2023",
#    "estado" : "A",
#    "integrantes" : [],
#    "cursos" : [1, 2, 4]
#    "msg" : "" | "msg" : "Hubo un error bla bla"
# } 
def verEquipo(request):
    if request.method == "GET":
        equipoId = request.GET.get("id")

        if equipoId == "":
            errorDict = {
                "msg" : "Debe enviar un id de equipo"
            }
            return HttpResponse(json.dumps(errorDict))
        
        try:
            equipo = Equipo.objects.get(pk=equipoId)
        except:
            errorDict = {
                "msg" : "Debe enviar un id de equipo que exista"
            }
            return HttpResponse(json.dumps(errorDict))
        
        respDict = {
            "id" : equipo.pk,
            "nombre" : equipo.nombre,
            "anho" : equipo.anho,
            "estado" : equipo.estado,
            "integrantes" : [],
            "cursos" : [],
            "msg" : ""
        }
        return HttpResponse(json.dumps(respDict))

def modificarEquipo(request):
    pass

# Path /proyectos/ver-cursos?idequipo=1
# Request:  Query parameter
# Response:
# {
#    msg : "" | "msg" : "Hubo un error en el query",
#    cursos : [
#        { "id" : 1, "nombre": "Progra Web"},
#        ...
#    ]
# }
def verCursosDisponibles(request):
    if request.method == "GET":
        idEquipo = request.GET.get("idequipo")

        if idEquipo == None:
            # Devolver todos los cursos
            cursos = Curso.objects.all()

            # list comprehension
            cursosDict = [{ "id" : curso.pk, "nombre" : curso.nombre } for curso in cursos]

            # cursosDict = []
            # for curso in cursos:
            #     cursosDict.append({
            #         "id" : curso.pk,
            #         "nombre" :curso.nombre
            #     })

            respDict = {
                "msg" : "",
                "cursos" : cursosDict
            }
            return HttpResponse(json.dumps(respDict))
        else:
            # Devolver los cursos que estan disponibles

            # 1. Obtener los ids de cursos que el equipo esta registrado
            equipoXCursoRegistrados = EquipoXCurso.objects.filter(equipo__pk = idEquipo)
            idcursosRegistrados = [ exc.curso.pk for exc in equipoXCursoRegistrados ]
            
            #2. Excluir cursos qe se encuentran registrados
            cursosDisponibles = Curso.objects.exclude(pk__in=idcursosRegistrados)

            cursosDisponiblesDict = [{ "id" : curso.pk, "nombre" : curso.nombre } for curso in cursosDisponibles] 
            respDict = {
                "msg" : "",
                "cursos" : cursosDisponiblesDict
            }
            return HttpResponse(json.dumps(respDict))