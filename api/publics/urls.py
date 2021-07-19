from rest_framework import urlpatterns, routers
from .views import PublicRetrieveModelMixin
from django.urls import path


urlpatterns = [
    path('/<int:pk>', PublicRetrieveModelMixin.as_view())
]