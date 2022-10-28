from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
import requests

def principal(request):
    if request.method == 'POST':
        carnet = request.POST.get('carnet', None)
        nombre = request.POST.get('nombre', None)
        respuesta = requests.post("http://localhost:8080/getDatos", data = {'carnet': carnet, 'nombre': nombre})
    return render(request, "principal.html")


def visualizar(request):
    template = loader.get_template("visualizar.html")
    respuesta = requests.get('http://localhost:8080/visualizar')
    print(respuesta)
    context = {
        'datos': respuesta.json()
    }
    return HttpResponse(template.render(context, request))


def HT2(request):
    return HttpResponse("201700659 \n Viany Paola Juárez Hernández")

'''
def home(request):
    template = loader.get_template("index.html")
    respuesta = requests.get('http://127.0.0.1:5000/estudiante')
    context = respuesta.json()
    return HttpResponse(template.render(context, request))
'''