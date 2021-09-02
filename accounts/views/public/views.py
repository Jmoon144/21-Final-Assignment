from accounts.models import User, DoorLog
from accounts.serializers import PublicSerializer, UserSerializer
from rest_framework import (exceptions, generics, permissions, serializers,
                            status, mixins)
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response

FEE_PER_COUNT = 1

class PublicUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_key = request.META.get('HTTP_AUTHORIZATION')
        self.validate_auth_key(auth_key)
        unit, password = auth_key[:4], auth_key[4:]

        if unit == '0000':
            raise exceptions.AuthenticationFailed('NOT_PUBLIC_USER')
        
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

class IsPublicUserReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        return bool(
            # request.method in permissions.SAFE_METHODS and not
            not request.user.is_superuser and
            request.user.is_authenticated
        )

class UserDetailView(generics.GenericAPIView):
    authentication_classes = [PublicUserAuthentication, ]
    permission_classes  = [IsPublicUserReadOnly,]
    queryset = User.objects.prefetch_related('doorlog_set')
    serializer_class = PublicSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            unit     = request.data['unit']
            password = request.data['password']
            public = User.objects.get(unit = unit, password = password)
            serializers = PublicSerializer(public)

            return Response(
                {
                    'public' : serializers.data
                }, status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {
                    'message' : '입력정보가 틀렸습니다.'
                }, status = status.HTTP_400_BAD_REQUEST
            )

# class DoorlogAPIView(
#                     generics.GenericAPIView):
    
#     queryset = DoorLog.objects.all()
#     serializer_class = DoorlogSerializer

#     def post(self, request, *args, **kwargs):
#         try:
#             unit = request.data['unit']
#             password = request.data['password']
#             user = User.objects.get(unit=unit, password=password)
#             serializers = DoorlogSerializer(user)

#             return Response(
#                 {
#                     'message' : '문이열렸습니다.'
#                 }, status=status.HTTP_201_CREATED
#             )
#         except User.DoesNotExist:
#             return Response(
#                 {
#                     'message' : '입력정보가 틀렸습니다.'
#                 }, status=status.HTTP_400_BAD_REQUEST
            # )