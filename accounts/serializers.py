from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['unit', 'password']

class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['unit', 'cost']
    
# class DoorlogSerializer(serializers.ModelSerializer):

#     class Meta:
#         models = User
#         fields = ['unit', 'password',]