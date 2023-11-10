from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import Client

from .serializers import (
    ClientSerializer,
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
