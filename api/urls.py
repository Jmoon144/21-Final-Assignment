from django.urls import path, include

urlpatterns = [
    path('/public', include('api.publics.urls'))
]
