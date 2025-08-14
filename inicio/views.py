from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):

    return render(request, "inicio.html")

def portal(request):

    return render(request, "portal_deportes.html")

    