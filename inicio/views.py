from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Deportes


def inicio(request):

    return render(request, "inicio.html")

def portal_deportes(request, deportes, edad, indumentaria):

    portal = Deportes(deportes=deportes, edad=edad, indumentaria=indumentaria)

    return render(request, "portal_deportes", {"deportes":portal })



# Create your views here.
    