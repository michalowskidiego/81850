from django.db import models

class Deportes(models.Model):
    deporte = models.CharField(max_length=20)
    edad = models.CharField(max_length=20)
    indumentaria = models.CharField(max_length=20)