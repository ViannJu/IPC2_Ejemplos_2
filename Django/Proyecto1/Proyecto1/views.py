from django.http import HttpResponse
import requests
from django.template import loader
from django.shortcuts import render

def home(request):
    template = loader.get_template("pagina.html")
    respuesta = requests.get('http://127.0.0.1:5000/estudiante')
    context = respuesta.json()
    return HttpResponse(template.render(context, request))