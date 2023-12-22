from django.urls import path
from .change_password.views import ChangePasswordAPIView
from .profile.views import UserProfileAPIView

urlpatterns = [
    path('change-password', ChangePasswordAPIView.as_view()),
    path('profile', UserProfileAPIView.as_view()),
]
