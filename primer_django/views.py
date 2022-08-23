from json import load
from multiprocessing import context
from unittest import loader
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


def probar_template(request):
    plantilla = loader.get_template('plantilla1.html') 
    contexto = context() # ??????
    documento_html = plantilla.render(contexto)
    return HttpResponse(plantilla)

