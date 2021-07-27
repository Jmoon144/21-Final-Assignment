from django.urls import path
from accounts.views.public.views import PublicUserDetailView

urlpatterns = [
    path('/public/<int:pk>', PublicUserDetailView.as_view()),
]
