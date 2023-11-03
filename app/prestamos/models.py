from django.db import models

# Create your models here.

class Fondo(models.Model):
    #id_prestamista
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

