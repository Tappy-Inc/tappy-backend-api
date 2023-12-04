from rest_framework import serializers

# Models
from domain.system.models import Gender

import logging
logger = logging.getLogger(__name__)


class ReadGenderSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system_management.genders.id.ReadGenderSerializer"
        model = Gender
        fields = [
            'id',
            'gender',
            'created_at',
            'updated_at'
        ]


class UpdateGenderSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system_management.genders.id.UpdateGenderSerializer"
        model = Gender
        fields = [
            'gender',
        ]


class DeleteGenderSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system_management.genders.id.DeleteGenderSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadGenderSerializer()
