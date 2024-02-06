from django.urls import path
from .forgot_password.views import ForgotPasswordAPIView
from .reset_password.views import ResetPasswordAPIView
from .validate_otp.views import ValidateOTPAPIView

urlpatterns = [
    path('forgot-password', ForgotPasswordAPIView.as_view()),
    path('reset-password', ResetPasswordAPIView.as_view()),
    path('validate-otp', ValidateOTPAPIView.as_view()),
]
