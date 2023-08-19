from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hola Mundo')

def detalle_usuario(request):
    return HttpResponse('detalle_usuario')