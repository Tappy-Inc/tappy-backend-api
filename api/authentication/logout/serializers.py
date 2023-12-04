from rest_framework import serializers

# Models
from django.contrib.auth.models import User


class LogoutSerializer(serializers.Serializer):
    detail = serializers.CharField()

    class Meta:
        ref_name = "authentication.logout.LogoutSerializer"


class ErrorDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()

    class Meta:
        ref_name = "authentication.logout.ErrorDetailSerializer"

