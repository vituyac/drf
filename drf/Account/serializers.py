from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    # firstName = serializers.CharField(source='first_name')
    # lastName = serializers.CharField(source='last_name')
    
    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'username', 'password')