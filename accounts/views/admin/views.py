from accounts.models import User
from accounts.serializers import PublicSerializer
from rest_framework import exceptions, generics, permissions, serializers
from rest_framework.authentication import BaseAuthentication

class AdminUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_key = request.META.get('HTTP_AUTHORIZATION')
        self.validate_auth_key(auth_key)
        unit, password = auth_key[:4], auth_key[4:]

        if unit != '0000':
            raise exceptions.AuthenticationFailed('NOT_ADMIN_USER')
        
        try:
            user = User.objects.get(unit = unit, password = password)
            return (user, None)

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('USER_DOSE_NOT_EXIST')

    def validate_auth_key(self, auth_key):
        if not auth_key or len(auth_key) !=8:
            raise exceptions.AuthenticationFailed('INVALID_AUTH_KEY')

        try:
            int(auth_key)
        except ValueError:
            raise exceptions.AuthenticationFailed('INVALID_CHARACTER_IN_AUTH_KEY')

class IsAdminUserOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        
        return bool(
            request.method in permissions.SAFE_METHODS and 
            request.user.is_superuser and
            request.user.is_authenticated
        )

class PublicListAPIView(generics.ListAPIView):
    queryset           = User.objects.all()
    serializer_class   = PublicSerializer
    permission_classes = [IsAdminUserOnly]
    authentication_classes = [AdminUserAuthentication, ]
