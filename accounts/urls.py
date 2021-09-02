from django.urls import path
from accounts.views.public.views import UserDetailView
from accounts.views.admin.views import PublicListAPIView

urlpatterns = [
    path('/public', UserDetailView.as_view()),
    path('/admin', PublicListAPIView.as_view()),
    # path('/door', DoorlogAPIView.as_view())
]