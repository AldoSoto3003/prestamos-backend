from django.contrib import auth

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from app.accounts.serializers import RegistrationSerializer

    
class RegistrationView(APIView):
    
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['reponse'] = 'El registro del usuario fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone_number'] = account.phone_number
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            }
        else:
            data = serializer.errors
            
        return Response(data)
    
class LoginView(APIView):
    
    def post(self,request):
        data = {}
        email = request.data.get('email')
        password = request.data.get('password')
        
        account = auth.authenticate(email=email,password=password)
        if account is not None:
            data['response'] = 'El login fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone_number'] = account.phone_number
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data)
        else:
            data['error'] = 'Credenciales incorrectas'
            return Response(data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)