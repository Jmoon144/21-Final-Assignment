from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from .serializer import PublicSerializer

from .models import Public

class PublicRetrieveModelMixin(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset           = Public.objects.all()
    serializer_class   = PublicSerializer
    permission_classes = [IsAuthenticated]
    lookup_field       = "number"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
