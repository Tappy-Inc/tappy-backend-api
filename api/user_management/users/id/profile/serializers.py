from rest_framework import serializers

# Models
from domain.user.models.User import User
from domain.user.models import Profile

import logging
logger = logging.getLogger(__name__)


class ReadProfileSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.users.id.profile.ReadProfileSerializer"
        model = Profile
        fields = [
            'id',
            'user',
            'bio',
            'gender',
            'civil_status',
            'employee_id',
            'birth_date',
            'manager',
            'mobile_number',
            'nationality'
        ]


class ReadUserSerializer(serializers.ModelSerializer):
    profile = ReadProfileSerializer(read_only=True)

    class Meta:
        ref_name = "user-management.users.id.profile.ReadUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined',
            'profile'
        ]
