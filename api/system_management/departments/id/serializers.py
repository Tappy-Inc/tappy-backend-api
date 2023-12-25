from rest_framework import serializers

# Models
from domain.system.models import Department

import logging
logger = logging.getLogger(__name__)


class ReadDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.departments.id.ReadDepartmentSerializer"
        model = Department
        fields = [
            'id',
            'department_name',
            'created_at',
            'updated_at'
        ]


class UpdateDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.departments.id.UpdateDepartmentSerializer"
        model = Department
        fields = [
            'department_name',
        ]


class DeleteDepartmentSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.departments.id.DeleteDepartmentSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadDepartmentSerializer()
