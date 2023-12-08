from rest_framework import serializers

# Models
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)


class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user_management.users.id.ReadUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined'
        ]


class UpdateUserSerializer(serializers.ModelSerializer):

    # Note: added this field to the serializer to allow for partial updates
    username = serializers.CharField(max_length=150, required=False)

    class Meta:
        ref_name = "user_management.users.id.UpdateUserSerializer"
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active'
        ]


class DeleteUserSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user_management.users.id.DeleteUserSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadUserSerializer()
