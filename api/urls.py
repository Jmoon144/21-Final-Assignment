from django.urls import path, include

urlpatterns = [
    path('/admin', include('api.admins.urls')),
]
