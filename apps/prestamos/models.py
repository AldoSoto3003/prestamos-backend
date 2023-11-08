from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Cliente(models.Model):
    phone_regex = RegexValidator(regex=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex],max_length=17,blank=False)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True)
    status =models.BooleanField(default=True)
    
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.nombre
    
class Prestamista(models.Model):
    pass    
class Fondo(models.Model):
    #id_prestamista
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

