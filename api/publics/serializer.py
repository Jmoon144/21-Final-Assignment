from rest_framework.serializers import ModelSerializer

from .models import Public

class PublicSerializer(ModelSerializer):

    class Meta:
        model = Public
        fields = ('number', 'cost')
