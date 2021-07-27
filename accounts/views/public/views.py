from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework import authentication
from accounts.models import User
from accounts.serializers import UserSerializer

FEE_PER_COUNT = 1

#custom authentication_classes
from rest_framework.authentication import BaseAuthentication

class PublicUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authentication = request.META.get('HTTP_AUTH', 'default')
        params = request.query_params.get('key')
        
    
class PublicUserDetailView(generics.RetrieveAPIView):
    authentication_classes = [PublicUserAuthentication,]
    queryset = User.objects.all()
    serializer_class = UserSerializer