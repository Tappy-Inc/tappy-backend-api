from rest_framework import serializers

# Models
from domain.system.models import Department

import logging
logger = logging.getLogger(__name__)


class ReadDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "system-management.departments.ReadDepartmentSerializer"
        model = Department
        fields = [
            'id',
            'department_name',
            'created_at',
            'updated_at'
        ]


class CreateDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.departments.CreateDepartmentSerializer"
        model = Department
        fields = [
            'department_name'
        ]


class PaginateReadDepartmentSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.departments.PaginateReadDepartmentSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadDepartmentSerializer(many=True)


class PaginateQueryReadDepartmentSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.departments.PaginateQueryReadDepartmentSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
