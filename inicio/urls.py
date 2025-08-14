from django.urls import path
from inicio.views import inicio, portal_deportes


urlpatterns = [
    path("inicio/", inicio),
    path("portal_deportes/<futbol>/<tenis>/<padel>", portal_deportes)
]
