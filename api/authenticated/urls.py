from django.urls import path
from .change_password.views import ChangePasswordAPIView

urlpatterns = [
    path('change-password', ChangePasswordAPIView.as_view()),
]
