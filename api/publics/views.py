from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Public
from .serializer import LoginSerializer, PublicSerializer

class LoginAPI(generics.GenericAPIView):
    serializer_class   = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            number = request.data['number']
            password = request.data['password']
            
            public = Public.objects.get(number = number, password = password)
            serializers = PublicSerializer(public)
            return Response(
                {
                    'public' : serializers.data
                }, status=status.HTTP_200_OK
            )
        except Public.DoesNotExist:
            return Response(
                {
                    'message': '입력정보가 틀렸습니다.'
                }, status=status.HTTP_400_BAD_REQUEST
            )
