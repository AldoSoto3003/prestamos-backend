from django.contrib import auth
from rest_framework import serializers
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Account

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'username',
            'password',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
        )
    def create(self, validated_data):

        if self.validated_data['password'] != self.validated_data['password2']:
            raise serializers.ValidationError({'error':'passwords no coinciden'})
        
        if Account.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'El email ya existe'})
        
        if Account.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error':'El username ya existe'})

        auth_user = Account.objects.create_user(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            password = self.validated_data['password'],
            phone_number = self.validated_data['phone_number'],
        )
        return auth_user
        

class UserLoginSerializer(serializers.Serializer):
    
    id         = serializers.CharField(read_only=True)
    email      = serializers.EmailField()
    username   = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name  = serializers.CharField(read_only=True)
    password   = serializers.CharField(max_length=128,write_only=True)
    access     = serializers.CharField(read_only=True)
    refresh    = serializers.CharField(read_only=True)
    role       = serializers.CharField(read_only=True)

    def create(self,validated_data):
        pass

    def update(self,instance,validated_data):
        pass

    def validate(self,data):
        email    = data['email']
        password = data['password']
        user = auth.authenticate(email=email, password=password)

        if user is None:
            status_code = status.HTTP_404_NOT_FOUND
            data = {
                'success':False,
                'status_code':status_code,
                'reponse':'Usuario no encontado',
            }

            raise serializers.ValidationError(detail=data,code=status.HTTP_401_UNAUTHORIZED)
        
        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token  = str(refresh.access_token)
            validation = {
                'id':user.id,
                'username':user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
                'access': access_token,
                'refresh': refresh_token,
            }

            return validation
        
        except Account.DoesNotExist:
            raise serializers.ValidationError('Credenciales incorrectas')

class AuthMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'   

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'email',
            'role'
        )