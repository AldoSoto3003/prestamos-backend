from django.contrib.auth.models import User

from rest_framework import serializers

from app.accounts.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only = True)
    
    class Meta:
        model = Account
        fields = ['username','email','password','password2','first_name','last_name','phone_number']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        error_messages = {
            ''
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error': 'El password de confirmacion no coincide'})
        
        if Account.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'El email del usuario ya existe'})
        
        if Account.objects.filter(email=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error':'El email del usuario ya existe'})
        
        account = Account.objects.create_user(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            password = self.validated_data['password'],   
        )
        
        account.phone_number = self.validated_data['phone_number']
    
        account.save()
        return account
        