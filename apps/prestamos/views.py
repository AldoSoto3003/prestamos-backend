from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import (
    Client,
    Fund,
    MoneyLender
    )

from .serializers import (
    ClientSerializer,
    FundSerializer,
    MoneyLenderSerializer,
)

class ClientListView(APIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        users = Client.objects.all()
        serializer = self.serializer_class(users, many=True)
        status_code = status.HTTP_200_OK
        data = {
            'success':True,
            'status_code':status_code,
            'response':'Ok',
            'client': serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)

class ClientByNameView(APIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self,name):
        try:
            return Client.objects.filter(first_name__icontains=name)
        except Client.DoesNotExist:
            data = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'response':'No se encontró al usuario',
            }
            raise ValidationError(data)
    
    def get(self,request,name):
        client = self.get_object(name)
        serializer = self.serializer_class(client, many=True)
        status_code = status.HTTP_200_OK
        data = {
            'success':True,
            'status_code':status_code,
            'response':'Ok',
            'clients': serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)

class ClientView(APIView):
    
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self,pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            data = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'response':'No se encontró al usuario',
            }
            raise ValidationError(data)
    
    def get(self,request,pk):
        user = self.get_object(pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.validate(data=request.data)
        
        if serializer.is_valid():
            client = serializer.save()
            status_code = status.HTTP_201_CREATED
            data = {
                'success':True,
                'status_code':status_code,
                'response':'El registro del cliente ha sido exitoso',
                'client': {
                    'id': serializer.data['id'],
                    'first_name':serializer.data['first_name'],
                    'last_name':serializer.data['last_name'],
                    'phone_number':serializer.data['phone_number'],
                    'address':serializer.data['address'],
                    'email':serializer.data['email'],
                }
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    def patch(self,request,pk):
        client = self.get_object(pk)
        serializer = self.serializer_class(client,request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        client = self.get_object(pk)
        client.delete()
        data = {
                'success': True,
                'status_code': status.HTTP_204_NO_CONTENT,
                'response':'Usuario {} {} eliminado'.format(client.first_name, client.last_name),
            }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

class MoneyLenderByNameView(APIView):
    serializer_class = MoneyLenderSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self,name):
        try:
            return MoneyLender.objects.filter(first_name__icontains=name)
        except MoneyLender.DoesNotExist:
            data = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'response':'No se encontró al usuario',
            }
            raise ValidationError(data)
    
    def get(self,request,name):
        moneylender = self.get_object(name)
        serializer = self.serializer_class(moneylender, many=True)
        status_code = status.HTTP_200_OK
        data = {
            'success':True,
            'status_code':status_code,
            'response':'Ok',
            'moneylenders': serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)

class MoneyLenderListView(APIView):
    serializer_class = MoneyLenderSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        users = MoneyLender.objects.all()
        serializer = self.serializer_class(users, many=True)
        status_code = status.HTTP_200_OK
        data = {
            'success':True,
            'status_code':status_code,
            'response':'Ok',
            'moneylenders': serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)

class MoneyLenderView(APIView):
    
    serializer_class = MoneyLenderSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self,pk):
        try:
            return MoneyLender.objects.get(pk=pk)
        except MoneyLender.DoesNotExist:
            data = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'response':'No se encontró al prestamista',
            }
            raise ValidationError(data)
    
    def get(self,request,pk):
        moneylender = self.get_object(pk)
        serializer = self.serializer_class(moneylender)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.validate(data=request.data)
        
        if serializer.is_valid():
            moneylender = serializer.save()
            status_code = status.HTTP_201_CREATED
            data = {
                'success':True,
                'status_code':status_code,
                'response':'El registro del prestamista ha sido exitoso',
                'prestamista': {
                    'id': serializer.data['id'],
                    'first_name':serializer.data['first_name'],
                    'last_name':serializer.data['last_name'],
                    'phone_number':serializer.data['phone_number'],
                    'address':serializer.data['address'],
                    'email':serializer.data['email'],
                }
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    def patch(self,request,pk):
        moneylender = self.get_object(pk)
        serializer = self.serializer_class(moneylender,request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        moneylender = self.get_object(pk)
        moneylender.delete()
        data = {
                'success': True,
                'status_code': status.HTTP_204_NO_CONTENT,
                'response':'Usuario {} {} eliminado'.format(moneylender.first_name, moneylender.last_name),
            }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    
class FundByMoneyLenderView(APIView):
    serializer_class = FundSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self,fk):
        try:
            return Fund.objects.get(moneylender=fk)
        except Fund.DoesNotExist:
            data = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'response':'No se encontró el fondo del prestamista',
            }
            raise ValidationError(data)

    
    def get(self,request,fk):
        fund = self.get_object(fk)
        serializer = self.serializer_class(fund,)
        status_code = status.HTTP_200_OK
        data = {
            'success':True,
            'status_code':status_code,
            'response':'Ok',
            'funds': serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)

class FundView(APIView):
    
    serializer_class = FundSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self,pk):
        try:
            return Fund.objects.get(pk=pk)
        except Fund.DoesNotExist:
            data = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'response':'No se encontró al fondo del prestamista',
            }
            raise ValidationError(data)
    
    def get(self,request,pk):
        fund = self.get_object(pk)
        serializer = self.serializer_class(fund)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            fund = serializer.save()
            status_code = status.HTTP_201_CREATED
            data = {
                'success':True,
                'status_code':status_code,
                'response':'Se ha registrado un fondo para el prestamista',
                'prestamista': {
                    'id': serializer.data['id'],
                    'amount':serializer.data['amount'],
                }
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    def patch(self,request,pk):
        return Response({'error':'esta vista está inhabilitada imbecil'},status=status.HTTP_400_BAD_REQUEST)
        fund = self.get_object(pk)
        serializer = self.serializer_class(fund,request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def delete(self,request,pk):
        fund = self.get_object(pk)
        fund.delete()
        data = {
                'success': True,
                'status_code': status.HTTP_204_NO_CONTENT,
                'response':'Fondo eliminado',
            }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    
