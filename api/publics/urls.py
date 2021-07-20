from .views import PublicRetrieveModelMixin
from django.urls import path

urlpatterns = [
    path('/<int:number>', PublicRetrieveModelMixin.as_view())
]