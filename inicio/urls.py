from django.urls import path
from inicio.views import inicio, portal


urlpatterns = [
    path("inicio/", inicio),
    path("portal_deportes/", portal)    
]
