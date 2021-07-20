from api.publics.models import Public
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Admin

class PublicSerializer(ModelSerializer):

    class Meta:
        model = Public
        fields = ('number', 'cost')

class AdminSerializer(ModelSerializer):
    publics = PublicSerializer(many=True, read_only=True, source='public_set')

    class Meta:
        model = Admin
        fields = ('id', 'password', 'publics')