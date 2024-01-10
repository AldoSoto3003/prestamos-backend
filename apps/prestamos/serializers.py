from django.contrib import auth
from rest_framework import serializers
from rest_framework import status
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Sum

from .models import Client,MoneyLender,Fund, Loan, LoanDetail

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

class MoneyLenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyLender
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
        )  
    
    def validate(self,data):
        
        moneylender_id = self.instance.id if self.instance else None
        
        if MoneyLender.objects.exclude(id=moneylender_id).filter(email=data.get('email')).exists():
            status_code = status.HTTP_400_BAD_REQUEST
            data = {
                "success":False,
                "status_code": status_code,
                "response":"Ya existe un prestamista con este email"
            }
            raise serializers.ValidationError(data, code=status.HTTP_400_BAD_REQUEST) 
        
        if MoneyLender.objects.exclude(id=moneylender_id).filter(phone_number=data.get('phone_number')).exists():
            status_code = status.HTTP_400_BAD_REQUEST
            data = {
                "success":False,
                "status_code": status_code,
                "response":"Ya existe un prestamista con este numero de telefono"
            }
            raise serializers.ValidationError(data, code=status.HTTP_400_BAD_REQUEST) 
        
        return data
    
class FundSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fund
        fields = '__all__'

    def validate(self,data):
        if Fund.objects.filter(moneylender_id=data.get('moneylender')).exists():
            status_code = status.HTTP_400_BAD_REQUEST
            data = {
                "success":False,
                "status_code": status_code,
                "response":"Ya existe un fondo para este prestamista"
            }
            raise serializers.ValidationError(data,status.HTTP_400_BAD_REQUEST) 
        return data

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
    
class GetAllLoanSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(source='client.first_name')
    remaining_amount = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = '__all__'
    
    def get_remaining_amount(self, obj):
        # Obtener el saldo inicial del préstamo
        initial_amount = obj.total_amount

        # Calcular la suma de los abonos para este préstamo
        total_payments = obj.payment_set.aggregate(total_payments=Sum('amount'))['total_payments'] or 0

        # Calcular el monto pendiente
        remaining_amount = initial_amount - total_payments

        return remaining_amount
    
class LoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDetail
        fields = (
            'moneylender',
            'amount'
        )