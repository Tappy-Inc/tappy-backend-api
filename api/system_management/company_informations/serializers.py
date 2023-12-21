from rest_framework import serializers

# Models
from domain.system.models import CompanyInformation

import logging
logger = logging.getLogger(__name__)


class ReadCompanyInformationSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "system-management.work_informations.ReadCompanyInformationSerializer"
        model = CompanyInformation
        fields = [
            'id',
            'company_name',
            'address',
            'number',
            'company_size',
            'industry',
            'created_at',
            'updated_at'
        ]


class CreateCompanyInformationSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.work_informations.CreateCompanyInformationSerializer"
        model = CompanyInformation
        fields = [
            'company_name',
            'address',
            'number',
            'company_size',
            'industry'
        ]


class PaginateReadCompanyInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.work_informations.PaginateReadCompanyInformationSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadCompanyInformationSerializer(many=True)


class PaginateQueryReadCompanyInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.work_informations.PaginateQueryReadCompanyInformationSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")

