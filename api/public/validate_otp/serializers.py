from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class ValidateOTPSerializer(serializers.Serializer):

    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=100)

    class Meta:
        ref_name = "public.validate_otp.ValidateOTPSerializer"

class ValidateOTPResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)

    class Meta:
        ref_name = "public.validate_otp.ValidateOTPResponseSerializer"

