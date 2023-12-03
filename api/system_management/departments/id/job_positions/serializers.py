from rest_framework import serializers

# Models
from domain.system.models import JobPosition

class ReadJobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "system-management.job-positions.ReadJobPositionSerializer"
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
        ref_name = "system-management.job-positions.CreateJobPositionSerializer"
        model = JobPosition
        fields = [
            'position_name',
        ]
