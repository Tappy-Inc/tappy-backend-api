from rest_framework import serializers

# Models
from domain.user.models import User

import logging
logger = logging.getLogger(__name__)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        ref_name = "public.forgot_password.ForgotPasswordSerializer"


class ForgotPasswordResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)

    class Meta:
        ref_name = "public.forgot_password.ForgotPasswordResponseSerializer"
