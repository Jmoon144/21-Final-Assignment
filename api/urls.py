from django.urls import path, include

urlpatterns = [
    path('/admin', include('api.admins.urls')),
    path('/public', include('api.publics.urls'))
]
