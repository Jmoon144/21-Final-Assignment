from api.publics.models import Public
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from .serializer import AdminSerializer

class PublicListAPIView(generics.ListAPIView):
    queryset           = Public.objects.all()
    serializer_class   = AdminSerializer
    permission_classes = [IsAuthenticated]