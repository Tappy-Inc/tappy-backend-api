from rest_framework import serializers

# Models
from domain.system.models import Gender

import logging
logger = logging.getLogger(__name__)


class ReadGenderSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "system_management.genders.ReadGenderSerializer"
        model = Gender
        fields = [
            'id',
            'gender',
            'created_at',
            'updated_at'
        ]


class CreateGenderSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system_management.genders.CreateGenderSerializer"
        model = Gender
        fields = [
            'gender'
        ]


class PaginateReadGenderSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system_management.genders.PaginateReadGenderSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadGenderSerializer(many=True)


class PaginateQueryReadGenderSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system_management.genders.PaginateQueryReadGenderSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
