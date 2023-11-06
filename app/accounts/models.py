from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    
    def create_user(self,email, password, **kwargs):
        
        if not email:
            raise ValueError('El usuario debe tener un email')
        
        if not password:
            raise ValueError('La usuario debe tener una contraseña')

        email = self.normalize_email(email=email)
        
        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('role', 1)
        
        if kwargs.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin')
        
        email = self.normalize_email(email=email)
        return self.create_user(email, password, **kwargs)

class Account(AbstractBaseUser, PermissionsMixin):
    
    ADMIN = 1
    PRESTAMISTA = 2
    CLIENTE = 3
    
    
    ROLE_CHOICES = (
        (ADMIN,'Admin'),
        (PRESTAMISTA, 'Prestamista'),
        (CLIENTE, 'Cliente')
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True,default=3) 
    
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now_add=True)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = CustomUserManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.email
    