from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()

#RegistrationSerializer

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, validators = [validate_password])
    password2 = serializers.CharField(write_only=True, validators = [validate_password])
    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2'
        ]
        
    #check if email already exist
    def validate_email(self,value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("Email already exist try again!")
        return value  
    
    #create account 
    def create(self, validated_data):
        email = validated_data.get('email')
        password =  validated_data.get('password1')
        User.objects.create_user(email=email, password=password)
        return validated_data
        
    #validate if both password are the same
    def validate(self, attrs):
        if attrs.get('password1') != attrs.get('password2'):
            raise serializers.ValidationError("Both password doesn't match")
        return attrs
    
#LoginSerializer

class LoginSerializer(TokenObtainPairSerializer):
    username_field = 'email'
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Both email and password are required.")

        data = super().validate(attrs) 
        data['email'] = self.user.email
        return data