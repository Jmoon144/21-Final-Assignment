from .views import LoginAPI
from django.urls import path

urlpatterns = [

    path('', LoginAPI.as_view())
]