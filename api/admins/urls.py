from django.contrib.auth.models import User
from rest_framework import urlpatterns, routers
from .views import PublicListAPIView
from django.urls import path

urlpatterns = [
    path('', PublicListAPIView.as_view()),
]