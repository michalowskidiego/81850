from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Esta es la pagina de inicio")

# Create your views here.
