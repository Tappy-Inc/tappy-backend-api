from rest_framework import serializers

# Models
from domain.user.models import Profile

import logging
logger = logging.getLogger(__name__)


class ReadProfileSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user_management.profiles.id.ReadProfileSerializer"
        model = Profile
        fields = [
            'id',
            'user',
            'bio',
            'location',
            'gender',
            'civil_status',
            'employee_id',
            'birth_date',
            'manager'
        ]


class UpdateProfileSerializer(serializers.ModelSerializer):

    # Note: added this field to the serializer to allow for partial updates
    # Note: added this to avoid serializer blocked, Because employee_id is unique serialize validate this field
    employee_id = serializers.CharField(max_length=150, required=False)

    class Meta:
        ref_name = "user_management.profiles.id.UpdateProfileSerializer"
        model = Profile
        fields = [
            'bio',
            'location',
            'gender',
            'civil_status',
            'employee_id',
            'birth_date',
            'manager'
        ]


class DeleteProfileSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user_management.profiles.id.DeleteProfileSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadProfileSerializer()
