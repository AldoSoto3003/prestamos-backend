from django.contrib import auth

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.accounts.models import Account

from .serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserListSerializer,
    AuthMeSerializer,
)

    
class RegistrationView(APIView):
    
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            status_code = status.HTTP_201_CREATED
            refresh = RefreshToken.for_user(account)
            data = {
                'success':True,
                'status_code':status_code,
                'reponse':'El registro del usuario fue exitoso',
                'user': {
                    'id':serializer.data['id'],
                    'username':serializer.data['username'],
                    'first_name':serializer.data['first_name'],
                    'last_name':serializer.data['last_name'],
                    'refresh': str(refresh),
                    'access':str(refresh.access_token),
                },
            }
        else:
            data = serializer.errors
            
        return Response(data)
    
class LoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)
    
    def post(self,request):
        data = {}
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_202_ACCEPTED
            data = {
                'success':True,
                'status_code':status_code,
                'reponse':'El login del usuario fue exitoso',
                'user': {
                    'id':serializer.data['id'],
                    'username':serializer.data['username'],
                    'first_name':serializer.data['first_name'],
                    'last_name':serializer.data['last_name'],
                    'refresh': serializer.data['refresh'],
                    'access': serializer.data['access'],
                },
            }
            return Response(data)

class LogoutView(APIView):
    
    permission_classes = [IsAuthenticated,]
    
    def post(self,request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status = status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AuthMeView(APIView):

    serializer_class = AuthMeSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        
        user = Account.objects.get(email=request.user)
        if user:
            print(user)
            status_code = status.HTTP_200_OK
            response = {
                'success':True,
                'status_code':status_code,
                'reponse':'El authme del usuario fue exitoso',
                'user': {
                    'id':user.id,
                    'email':user.email,
                    'username':user.username,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'rol':user.role,
                },
            }    
        return Response(response, status=status.HTTP_200_OK)
        
class UserListView(APIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user
        if user.role != 1:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            users = Account.objects.all()
            serializer = self.serializer_class(users, many=True)
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Successfully fetched users',
                'users': serializer.data

            }
            return Response(response, status=status.HTTP_200_OK)