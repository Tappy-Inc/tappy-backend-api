from rest_framework import serializers

# Models
from domain.user.models import WorkInformation
from domain.user.models.User import User

from domain.system.models import Department
from domain.system.models import JobLevel
from domain.system.models import EmploymentType
from domain.system.models import WorkSetup

import logging
logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.UserSerializer"
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.DepartmentSerializer"
        model = Department
        fields = ['id', 'department_name']


class JobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.JobLevelSerializer"
        model = JobLevel
        fields = ['id', 'level']


class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.EmploymentTypeSerializer"
        model = EmploymentType
        fields = ['id', 'employment_type']


class WorkSetupSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.WorkSetupSerializer"
        model = WorkSetup
        fields = ['id', 'work_setup']


class ReadWorkInformationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    job_level = JobLevelSerializer(read_only=True)
    employment_type = EmploymentTypeSerializer(read_only=True)
    work_setup = WorkSetupSerializer(read_only=True)

    class Meta:
        ref_name = "user-management.work-informations.ReadWorkInformationSerializer"
        model = WorkInformation
        fields = [
            'id',
            'user',
            'department',
            'job_level',
            'employment_type',
            'work_setup'
        ]


class CreateWorkInformationSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.work-informations.CreateWorkInformationSerializer"
        model = WorkInformation
        fields = [
            'user',
            'department',
            'job_level',
            'employment_type',
            'work_setup'
        ]


class PaginateReadWorkInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.work-informations.PaginateReadWorkInformationSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadWorkInformationSerializer(many=True)


class PaginateQueryReadWorkInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.work-informations.PaginateQueryReadWorkInformationSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
