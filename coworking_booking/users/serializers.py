from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fileds = ['id', 'username', 'email', 'phone']

class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User .objects.all())]
    )
    password = serializers.CharField(
        write_only = True, 
        required = True,
        validators = [validate_password]
    )
    password2 = serializers.CharField(
        write_only = True, 
        required = True,
        validators = [validate_password]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password incorrect'})
        return attrs
    
    def create(self, validate_data):
        user = User.objects.create(
            username = validate_data['username'],
            email  = validate_data['email'],
            phone = validate_data.get('phone', None)
        )
        user.set_password(validate_data['password'])
        user.save()
        return user