from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import PublicSerializer

from .models import Public

class PublicListModelMixin(mixins.ListModelMixin, generics.GenericAPIView):
    queryset           = Public.objects.all()
    serializer_class   = PublicSerializer
    permission_classes = [IsAuthenticated]
    filter_backends    = [DjangoFilterBackend]
    filterset_fields   = ['number', 'password']
    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
