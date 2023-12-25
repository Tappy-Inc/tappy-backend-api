from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):

    class Meta:
        ref_name = "authenticated.change-password.ChangePasswordSerializer"

    existing_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128, validators=[validate_password])
    password_confirmation = serializers.CharField(max_length=128, validators=[validate_password])

    def validate(self, data):
        if data['new_password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords must match.")
        return data


class ChangePasswordResponseSerializer(serializers.Serializer):

    class Meta:
        ref_name = "authenticated.change-password.ChangePasswordResponseSerializer"

    message = serializers.CharField(max_length=256)
