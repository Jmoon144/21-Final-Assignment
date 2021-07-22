from api.publics.models import Public
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class AdminSerializer(ModelSerializer):

    class Meta:
        model  = Public
        fields = ('number', 'cost', 'password')