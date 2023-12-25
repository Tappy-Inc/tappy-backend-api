from rest_framework import serializers

# Models
from domain.system.models import EmploymentType

import logging
logger = logging.getLogger(__name__)


class ReadEmploymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.employment-types.id.ReadEmploymentTypeSerializer"
        model = EmploymentType
        fields = [
            'id',
            'employment_type',
            'created_at',
            'updated_at'
        ]


class UpdateEmploymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.employment-types.id.UpdateEmploymentTypeSerializer"
        model = EmploymentType
        fields = [
            'employment_type',
        ]


class DeleteEmploymentTypeSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.employment-types.id.DeleteEmploymentTypeSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadEmploymentTypeSerializer()
