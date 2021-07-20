from rest_framework import mixins, generics
from .serializer import PublicSerializer

from .models import Public

class PublicRetrieveModelMixin(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset         = Public.objects.all()
    serializer_class = PublicSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
