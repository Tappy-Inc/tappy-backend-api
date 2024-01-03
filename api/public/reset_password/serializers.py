from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class ResetPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()
    reset_code = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=128)
    password_confirmation = serializers.CharField(max_length=128)

    def validate(self, data):
        if data['new_password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords do not match")
        validate_password(data['new_password'])
        return data

    class Meta:
        ref_name = "public.reset_password.ResetPasswordSerializer"

class ResetPasswordResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)

    class Meta:
        ref_name = "public.reset_password.ResetPasswordResponseSerializer"

