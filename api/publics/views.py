from rest_framework import mixins, viewsets, generics, status

from .models import Public
from .serializer import PublicSerializer

class PublicRetrieveModelMixin(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)