from rest_framework import serializers

# Models
from domain.user.models.User import User

import logging
logger = logging.getLogger(__name__)


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.users.ReadUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'is_active',
            'date_joined',
            'last_login'
        ]


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.users.CreateUserSerializer"
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        ]


class PaginateReadUserSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.users.PaginateReadUserSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadUserSerializer(many=True)


class PaginateQueryReadUserSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.users.PaginateQueryReadUserSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
