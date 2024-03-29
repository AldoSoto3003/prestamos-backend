from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

from .base.base_models import BaseModel,BaseModelManager

class Client(BaseModel):
    phone_regex = RegexValidator(regex=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,blank=False, unique=True)
    phone_number = models.CharField(validators=[phone_regex],max_length=17,blank=False,unique=True)
    address = models.CharField(max_length=100)
    status =models.BooleanField(default=True)
    
    objects = BaseModelManager()
    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.first_name + self.last_name
    
class MoneyLender(BaseModel):
    phone_regex = RegexValidator(regex=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,blank=False, unique=True)
    phone_number = models.CharField(validators=[phone_regex],max_length=17,blank=False, unique=True)
    address = models.CharField(max_length=100)
    status =models.BooleanField(default=True)
    
    objects = BaseModelManager()
    
    class Meta:
        verbose_name = ("MoneyLender")
        verbose_name_plural = ("MoneyLenders")
    
    def __str__(self):
        return self.first_name + self.last_name
    
class Fund(BaseModel):
    moneylender = models.ForeignKey(MoneyLender, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    objects = BaseModelManager()

class Loan(BaseModel):

    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    interest_rate = models.DecimalField(max_digits=10,decimal_places=2)
    # balance = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField(blank=False)

    objects = BaseModelManager()

    def save(self, *args, **kwargs):
        # Calcula el total_amount solo si el objeto es nuevo
        if not self.id:
            self.total_amount = self.subtotal * ((self.interest_rate / 100) + 1)

        # Llama al método save del modelo base
        super(Loan, self).save(*args, **kwargs)

class LoanDetail(BaseModel):

    loan = models.ForeignKey(Loan,on_delete=models.CASCADE)
    moneylender = models.ForeignKey(MoneyLender,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    objects = BaseModelManager()

class Payment(BaseModel):

    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField(blank=False)

    objects = BaseModelManager()

class PaymentDetail(BaseModel):

    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    moneylender = models.ForeignKey(MoneyLender,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    objects = BaseModelManager()
    