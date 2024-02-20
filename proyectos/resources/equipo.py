from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from proyectos.models import Equipo, EquipoXCurso, Integrante, Curso

@csrf_exempt
def equipoResource(request):
    if request.method == "GET":
        # Devuelve la lista de todos los equipos
        # Es una peticion de tipo GET
        nombreFiltro = request.GET.get("nombre") # Obtenemos query parameter nombre
        anhoFiltro = request.GET.get("anho")

        if (nombreFiltro == "" or nombreFiltro == None) and (anhoFiltro == "-" or anhoFiltro == None):
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
    elif request.method == "POST":
        # Registra un nuevo equipo
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
    elif request.method == "PUT":
        # Modifica un equipo existente
        pass
    elif request.method == "DELETE":
        # Elimina un equipo existente
        id = request.GET.get("id")
        equipoAEliminar = Equipo.objects.get(pk=id)
        if equipoAEliminar == None:
            # Error, equipo no existe
            respDict = {
                "msg" : "No existe el recurso a eliminar"
            }
            return HttpResponse(json.dumps(respDict))

        equipoAEliminar.delete()

        respDict = {
            "msg" : ""
        }
        return HttpResponse(json.dumps(respDict))

def equipoInfoResource(request, equipoid):
    if request.method == "GET":
        equipo = Equipo.objects.get(pk=equipoid)

        if equipo == None:
            respDict = {
                "msg" : "Recurso no existe"
            }
            return HttpResponse(json.dumps(respDict))
        
        integrantes = Integrante.objects.filter(equipo=equipo)
        equipoXCurso = EquipoXCurso.objects.filter(equipo=equipo)

        integrantesDict = [{ "codigo": inte.codigo,"nombre" : inte.nombre } for inte in integrantes ]

        cursosDict = []
        for ec in equipoXCurso:
            curso = ec.curso
            cursosDict.append({
                "id" : curso.id,
                "nombre" : curso.nombre
            })

        respDict = {
            "id" : equipo.id,
            "nombre" : equipo.nombre,
            "anho" : equipo.anho,
            "integrantes" : integrantesDict,
            "cursos" : cursosDict,
            "msg" : ""
        }
        return HttpResponse(json.dumps(respDict))

