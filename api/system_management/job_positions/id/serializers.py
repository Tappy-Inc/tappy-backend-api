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


class UpdateJobPositionSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.job-positions.id.UpdateJobPositionSerializer"
        model = JobPosition
        fields = [
            'position_name',
            'department'
        ]


class DeleteJobPositionSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.job-positions.id.DeleteJobPositionSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadJobPositionSerializer()
