from rest_framework import serializers

# Models
from domain.system.models import JobPosition

import logging
logger = logging.getLogger(__name__)


class ReadJobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "system-management.job-positions.id.ReadJobPositionSerializer"
        model = JobPosition
        fields = [
            'id',
            'position_name',
            'department',
            'created_at',
            'updated_at'
        ]


class CreateJobPositionSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.job-positions.id.CreateJobPositionSerializer"
        model = JobPosition
        fields = [
            'position_name',
            'department'
        ]


class PaginateReadJobPositionSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.job-positions.id.PaginateReadJobPositionSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadJobPositionSerializer(many=True)


class PaginateQueryReadJobPositionSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.job-positions.id.PaginateQueryReadJobPositionSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
