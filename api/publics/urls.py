from .views import PublicListModelMixin
from django.urls import path

urlpatterns = [

    path('', PublicListModelMixin.as_view())
]