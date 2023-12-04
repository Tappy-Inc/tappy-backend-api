from rest_framework import serializers

# Models
from django.contrib.auth.models import User



class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "authentication.login.ReadUserSerializer"
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        ref_name = "authentication.login.LoginSerializer"


class ReadCredentialSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    user = ReadUserSerializer(read_only=True)

    class Meta:
        ref_name = "authentication.login.ReadCredentialSerializer"


class ErrorDetailSerializer(serializers.Serializer):
    detail = serializers.CharField()

    class Meta:
        ref_name = "authentication.login.ErrorDetailSerializer"

