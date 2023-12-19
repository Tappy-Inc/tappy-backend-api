from rest_framework import serializers

# Models
from domain.user.models import WorkInformation
from django.contrib.auth.models import User

from domain.system.models import Department
from domain.system.models import JobLevel

import logging
logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name']


class JobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = ['id', 'level']


class ReadWorkInformationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    job_level = JobLevelSerializer(read_only=True)

    class Meta:
        ref_name = "user-management.work_informations.ReadWorkInformationSerializer"
        model = WorkInformation
        fields = [
            'id',
            'user',
            'department',
            'job_level'
        ]


class CreateWorkInformationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    job_level = serializers.PrimaryKeyRelatedField(queryset=JobLevel.objects.all())

    class Meta:
        ref_name = "user-management.work_informations.CreateWorkInformationSerializer"
        model = WorkInformation
        fields = [
            'user',
            'department',
            'job_level'
        ]


class PaginateReadWorkInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.work_informations.PaginateReadWorkInformationSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadWorkInformationSerializer(many=True)


class PaginateQueryReadWorkInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.work_informations.PaginateQueryReadWorkInformationSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
