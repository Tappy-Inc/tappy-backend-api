from rest_framework import serializers

# Models
from domain.user.models.User import User
from domain.user.models import Profile

import logging
logger = logging.getLogger(__name__)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "authenticated.profile.ProfileSerializer"
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

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        ref_name = "authenticated.profile.UserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'is_active',
            'date_joined',
            'profile'
        ]
