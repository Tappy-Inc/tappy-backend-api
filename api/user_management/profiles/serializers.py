from rest_framework import serializers

# Models
from domain.user.models import Profile

import logging
logger = logging.getLogger(__name__)


class ReadProfileSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.profiles.ReadProfileSerializer"
        model = Profile
        fields = [
            'id',
            'user',
            'bio',
            'gender',
            'civil_status',
            'employee_id',
            'birth_date',
            'manager'
        ]


class CreateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.profiles.CreateProfileSerializer"
        model = Profile
        fields = [
            'user',
            'bio',
            'gender',
            'civil_status',
            'employee_id',
            'birth_date',
            'manager'
        ]


class PaginateReadProfileSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.profiles.PaginateReadProfileSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadProfileSerializer(many=True)


class PaginateQueryReadProfileSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.profiles.PaginateQueryReadProfileSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
