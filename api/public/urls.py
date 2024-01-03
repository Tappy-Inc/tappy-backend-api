from django.urls import path
from .forgot_password.views import ForgotPasswordAPIView
from .reset_password.views import ResetPasswordAPIView


urlpatterns = [
    path('forgot-password', ForgotPasswordAPIView.as_view()),
    path('reset-password', ResetPasswordAPIView.as_view()),
]
