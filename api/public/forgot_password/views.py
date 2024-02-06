from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Serializers
from .serializers import ForgotPasswordSerializer, ForgotPasswordResponseSerializer

# Services
from domain.user.services.user import get_user_by_email
from domain.user.caches.email import store_reset_password_otp_code

# Resend
from domain.mailer.services.resend import send_forgot_password_email

# Library: django-redis
from django.core.cache import cache

# Generating OTP
import random

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class ForgotPasswordAPIView(APIView):

    permission_classes = (AllowAny,)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        request_body=ForgotPasswordSerializer,
        responses={
            200: ForgotPasswordResponseSerializer()
        },
        operation_id="forgot_password",
        tags=["public"],
    )
    def post(request, *args, **kwargs):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_by_email(email=serializer.validated_data['email'])
        if user is None:
            return Response({"message": "User with this email does not exist."}, status=400)

        otp_code = random.randint(100000, 999999)
        store_reset_password_otp_code(email=user.email, otp_code=otp_code, expiry=300)
        send_forgot_password_email(email=user.email, opt_code=otp_code)

        response_serializer = ForgotPasswordResponseSerializer(data={"message": "Password reset email has been sent."})
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data)
