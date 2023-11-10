from django.contrib import auth
from rest_framework import serializers
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Client,MoneyLender,Fondo

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'email',
        )  
    
    def validate(self,data):
        
        client_id = self.instance.id if self.instance else None
        
        if Client.objects.exclude(id=client_id).filter(email=data.get('email')).exists():
            status_code = status.HTTP_400_BAD_REQUEST
            data = {
                "success":False,
                "status_code": status_code,
                "response":"Ya existe un cliente con este email"
            }
            raise serializers.ValidationError(data, code=status.HTTP_400_BAD_REQUEST) 
        
        if Client.objects.exclude(id=client_id).filter(phone_number=data.get('phone_number')).exists():
            status_code = status.HTTP_400_BAD_REQUEST
            data = {
                "success":False,
                "status_code": status_code,
                "response":"Ya existe un cliente con este numero de telefono"
            }
            raise serializers.ValidationError(data, code=status.HTTP_400_BAD_REQUEST) 
        
        return data