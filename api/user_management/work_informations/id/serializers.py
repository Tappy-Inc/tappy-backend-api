from rest_framework import serializers

# Models
from domain.user.models import WorkInformation
from domain.system.models import Department, JobLevel, EmploymentType, WorkSetup
from domain.user.models.User import User

import logging
logger = logging.getLogger(__name__)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.id.DepartmentSerializer"
        model = Department
        fields = ['id', 'department_name']

class JobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.id.JobLevelSerializer"
        model = JobLevel
        fields = ['id', 'level']

class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.id.EmploymentTypeSerializer"
        model = EmploymentType
        fields = ['id', 'employment_type']

class WorkSetupSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-informations.id.WorkSetupSerializer"
        model = WorkSetup
        fields = ['id', 'work_setup']

class ReadWorkInformationSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    job_level = JobLevelSerializer()
    employment_type = EmploymentTypeSerializer()
    work_setup = WorkSetupSerializer()

    class Meta:
        ref_name = "user-management.work-informations.id.ReadWorkInformationSerializer"
        model = WorkInformation
        fields = [
            'id',
            'user',
            'department',
            'job_level',
            'employment_type',
            'work_setup'
        ]

class UpdateWorkInformationSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=False)
    job_level = serializers.PrimaryKeyRelatedField(queryset=JobLevel.objects.all(), required=False)
    employment_type = serializers.PrimaryKeyRelatedField(queryset=EmploymentType.objects.all(), required=False)
    work_setup = serializers.PrimaryKeyRelatedField(queryset=WorkSetup.objects.all(), required=False)

    class Meta:
        ref_name = "user-management.work-informations.id.UpdateWorkInformationSerializer"
        model = WorkInformation
        fields = [
            'department',
            'job_level',
            'employment_type',
            'work_setup'
        ]

class DeleteWorkInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.work-informations.id.DeleteWorkInformationSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadWorkInformationSerializer()
