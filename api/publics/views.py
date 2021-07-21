from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Public
from .serializer import LoginSerializer, PublicSerializer

# class PublicListModelMixin(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset           = Public.objects.all()
#     serializer_class   = PublicSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends    = [DjangoFilterBackend]
#     filterset_fields   = ['number', 'password']

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class PublicListAPIView(generics.ListAPIView):
#     queryset = Public.objects.all()
#     serializer_class = PublicSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields=('number','password')

# def list(self, request):
#     queryset = self.get_queryset()
#     filter_backends = self.filter_queryset(queryset)
#     serializer = PublicSerializer(filter_backends, many=True)
#     return Response(serializer.data)

class LoginAPI(generics.GenericAPIView):
    serializer_class   = LoginSerializer
    permission_classes = [IsAuthenticated]

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
                }, status=status.HTTP_401_UNAUTHORIZED
            )
