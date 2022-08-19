from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola comision 41220")

def segunda_vista(request):
    return HttpResponse("prueba de views")

def dia_de_hoy(request):
    dia = datetime.now()
    texto = f"hoy es dia: {dia}"
    return HttpResponse(texto)


def mi_nombre_es(request, nombre):
    texto = f"mi nombre es {nombre}"
    return HttpResponse(texto)