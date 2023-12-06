from rest_framework import serializers

# Models
from domain.system.models import EmploymentType

import logging
logger = logging.getLogger(__name__)


class ReadEmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "system-management.employment-types.ReadEmploymentTypeSerializer"
        model = EmploymentType
        fields = [
            'id',
            'employment_type',
            'created_at',
            'updated_at'
        ]


class CreateEmploymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.employment-types.CreateEmploymentTypeSerializer"
        model = EmploymentType
        fields = [
            'employment_type'
        ]


class PaginateReadEmploymentTypeSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.employment-types.PaginateReadEmploymentTypeSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadEmploymentTypeSerializer(many=True)


class PaginateQueryReadEmploymentTypeSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.employment-types.PaginateQueryReadEmploymentTypeSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")

