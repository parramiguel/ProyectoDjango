from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):
        
        self.nombre=nombre

        self.apellido=apellido

def saludo(request): #Primera vista

    p1=Persona(" Operador Miguel", "Parra")
    
    #nombre= " Miguel"

    #apellido= " Parra"
    temasDelCurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    #temasDelCurso=[]

    ahora=datetime.datetime.now()

    #doc_externo=open("C:/Users/Asus/Documents/ProyectoDjango/Proyecto1/Proyecto1/Plantillasmiplantilla.html")
    
    #plt=Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo=get_template('miplantilla.html')

    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido,"En_estos_momento_es":ahora, "Temas":temasDelCurso})

    #texto=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido,"En_estos_momento_es":ahora, "Temas":temasDelCurso})
    
    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido,"En_estos_momento_es":ahora, "Temas":temasDelCurso})

def CursoH(request):

    Fecha_Actual=datetime.datetime.now() 

    return render(request, "CursoH.html", {"dameFecha":Fecha_Actual})

def despedida(request): #Segunda Vista

    return HttpResponse("Hasta Luego estimado")

def damefecha(request):

    Fecha_Actual=datetime.datetime.now()

    texto="""<html>
    <body>
    <h2>
    Fecha y Hora actuales %s
    </h2>
    </body>
    </html>""" % Fecha_Actual

    return HttpResponse(texto)

def calculaEdad(request, edad, agno):

    #edadActual=18
    periodo=agno-2024
    edadFutura=edad+periodo
    texto="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

    return HttpResponse(texto)